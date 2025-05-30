from __future__ import annotations

import logging
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DATA_COORDINATOR, DATA_DEVICE
from .dps_metadata import DPS_METADATA

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Richte schaltbare Entitäten für den Wechselrichter ein."""
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    api = hass.data[DOMAIN][entry.entry_id][DATA_DEVICE]

    entities = []

    for dps_code, meta in DPS_METADATA.items():
        if meta["type"] == "bool" and meta.get("writable", False):
            entities.append(DabbssonSwitch(coordinator, api, dps_code, meta))

    async_add_entities(entities)


class DabbssonSwitch(CoordinatorEntity, SwitchEntity):
    """Ein schaltbarer boolescher Wert aus dem Wechselrichter."""

    def __init__(self, coordinator, api, dps_code: str, meta: dict):
        super().__init__(coordinator)
        self.api = api
        self._dps_code = dps_code
        self._meta = meta
        self._attr_name = meta["name"]
        self._attr_unique_id = f"{api.device_id}_{dps_code}"

    @property
    def is_on(self) -> bool:
        """Gibt an, ob der Schalter eingeschaltet ist."""
        return bool(self.coordinator.data.get(self._dps_code))

    async def async_turn_on(self, **kwargs):
        """Aktiviere den Schalter."""
        if await self.api.send_command(self._dps_code, True):
            await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Deaktiviere den Schalter."""
        if await self.api.send_command(self._dps_code, False):
            await self.coordinator.async_request_refresh()