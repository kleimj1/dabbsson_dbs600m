from __future__ import annotations

import logging
from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DATA_COORDINATOR, DATA_DEVICE
from .dps_metadata import DPS_METADATA

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Setzt steuerbare numerische Werte als NumberEntity."""
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    api = hass.data[DOMAIN][entry.entry_id][DATA_DEVICE]

    entities = [
        DabbssonNumber(coordinator, api, dps_code, meta)
        for dps_code, meta in DPS_METADATA.items()
        if meta["type"] == "value" and meta.get("writable", False)
    ]

    async_add_entities(entities)


class DabbssonNumber(CoordinatorEntity, NumberEntity):
    """Numerischer Steuerwert des Wechselrichters."""

    def __init__(self, coordinator, api, dps_code: str, meta: dict):
        super().__init__(coordinator)
        self.api = api
        self._dps_code = dps_code
        self._meta = meta

        self._attr_name = meta["name"]
        self._attr_unique_id = f"{api.device_id}_{dps_code}"
        self._attr_native_unit_of_measurement = meta.get("unit")
        self._attr_native_min_value = meta.get("min", 0)
        self._attr_native_max_value = meta.get("max", 100)
        self._attr_native_step = meta.get("step", 1)

    @property
    def native_value(self) -> float:
        """Gibt den aktuellen Wert zurück."""
        return self.coordinator.data.get(self._dps_code)

    async def async_set_native_value(self, value: float):
        """Setzt einen neuen numerischen Wert."""
        code = self._meta.get("code", self._dps_code)
        int_value = int(round(value))

        if not self.api.is_online:
            _LOGGER.warning("⚠️ Gerät offline – setze %s nicht auf %s", code, int_value)
            return

        if await self.api.send_command(code, int_value):
            _LOGGER.info("✅ Setze %s auf %s", code, int_value)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.error("❌ Setzen von %s auf %s fehlgeschlagen", code, int_value)
