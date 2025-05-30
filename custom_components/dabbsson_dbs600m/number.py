from __future__ import annotations

import logging
from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DATA_COORDINATOR, DATA_DEVICE
from .dps_metadata import DPS_METADATA

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    api = hass.data[DOMAIN][entry.entry_id][DATA_DEVICE]
    entities = []

    for dps_code, meta in DPS_METADATA.items():
        if meta["type"] == "value" and meta.get("writable", False):
            entities.append(DabbssonNumber(coordinator, api, dps_code, meta))

    async_add_entities(entities)


class DabbssonNumber(CoordinatorEntity, NumberEntity):
    def __init__(self, coordinator, api, dps_code: str, meta: dict):
        super().__init__(coordinator)
        self.api = api
        self._dps_code = dps_code
        self._meta = meta
        self._attr_name = meta["name"]
        self._attr_unique_id = f"{api.device_id}_{dps_code}"
        self._attr_native_unit_of_measurement = meta.get("unit")
        self._attr_native_min_value = 0
        self._attr_native_max_value = 100
        self._attr_native_step = 1

    @property
    def native_value(self) -> float:
        return self.coordinator.data.get(self._dps_code)

    async def async_set_native_value(self, value: float):
        code = self._meta.get("code", self._dps_code)
        if await self.api.send_command(code, value):
            await self.coordinator.async_request_refresh()
