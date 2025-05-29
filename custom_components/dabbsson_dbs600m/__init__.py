from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, PLATFORMS, DATA_COORDINATOR, DATA_DEVICE
from .api import TuyaDeviceApi, DabbssonCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup der Dabbsson DBS600M Integration über das UI."""
    hass.data.setdefault(DOMAIN, {})

    api = TuyaDeviceApi(
        entry.data["client_id"],
        entry.data["client_secret"],
        entry.data["device_id"],
        entry.data["api_endpoint"],
    )
    await api.connect()  # <--- Wichtig: await, da async Methode

    coordinator = DabbssonCoordinator(hass, api, entry.data["name"])
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = {
        DATA_COORDINATOR: coordinator,
        DATA_DEVICE: api,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entferne eine Integration."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok