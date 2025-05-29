from __future__ import annotations

import logging
from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DATA_COORDINATOR, DATA_DEVICE
from .dps_metadata import DPS_METADATA

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Setze alle enum-Optionen als SelectEntity."""
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    api = hass.data[DOMAIN][entry.entry_id][DATA_DEVICE]

    entities = []

    for dps_code, meta in DPS_METADATA.items():
        if meta["type"] == "enum":
            entities.append(DabbssonSelect(coordinator, api, dps_code, meta))

    async_add_entities(entities)


class DabbssonSelect(CoordinatorEntity, SelectEntity):
    """Dropdown-Auswahl für enum-DPS."""

    def __init__(self, coordinator, api, dps_code: str, meta: dict):
        super().__init__(coordinator)
        self.api = api
        self._dps_code = dps_code
        self._meta = meta

        self._attr_name = meta["name"]
        self._attr_unique_id = f"{api.device_id}_{dps_code}"
        self._attr_options = meta.get("options", [])

    @property
    def current_option(self) -> str:
        """Gibt die aktuell gewählte Option zurück."""
        return str(self.coordinator.data.get(self._dps_code))

    async def async_select_option(self, option: str):
        """Setzt eine neue Option."""
        if self.api.send_command(self._dps_code, option):
            await self.coordinator.async_request_refresh()
