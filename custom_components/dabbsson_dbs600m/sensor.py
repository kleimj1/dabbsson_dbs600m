from __future__ import annotations

import logging
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.const import (
    UnitOfEnergy,
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfTemperature,
    UnitOfPower,
    UnitOfTime,
    PERCENTAGE,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DATA_COORDINATOR, DATA_DEVICE
from .dps_metadata import DPS_METADATA

_LOGGER = logging.getLogger(__name__)

UNIT_MAP = {
    "kW·h": UnitOfEnergy.KILO_WATT_HOUR,
    "W": UnitOfPower.WATT,
    "V": UnitOfElectricPotential.VOLT,
    "A": UnitOfElectricCurrent.AMPERE,
    "℃": UnitOfTemperature.CELSIUS,
    "%": PERCENTAGE,
    "s": UnitOfTime.SECONDS,
    "Kg": "kg",
    "pcs": "pcs"
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Richte Sensors für dabbsson_dbs600m ein."""
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    api = hass.data[DOMAIN][entry.entry_id][DATA_DEVICE]
    entities = []

    for dps_code, meta in DPS_METADATA.items():
        if meta["type"] in ("value", "string") and not meta.get("writable", False):
            entities.append(DabbssonSensor(coordinator, dps_code, meta))

    # Online-Status als zusätzliche Entität hinzufügen
    entities.append(DabbssonOnlineStatus(coordinator, api))

    async_add_entities(entities)


class DabbssonSensor(CoordinatorEntity, SensorEntity):
    """Repräsentiert einen readonly Sensor vom Wechselrichter."""

    def __init__(self, coordinator, dps_code: str, meta: dict):
        super().__init__(coordinator)
        self._attr_name = meta["name"]
        self._attr_unique_id = f"{coordinator.api.device_id}_{dps_code}"
        self._dps_code = dps_code
        self._meta = meta

        unit = meta.get("unit")
        self._attr_native_unit_of_measurement = UNIT_MAP.get(unit, unit)
        self._attr_device_class = self._guess_device_class(self._attr_native_unit_of_measurement)

    def _guess_device_class(self, unit: str | None):
        if unit == UnitOfTemperature.CELSIUS:
            return SensorDeviceClass.TEMPERATURE
        elif unit == UnitOfElectricPotential.VOLT:
            return SensorDeviceClass.VOLTAGE
        elif unit == UnitOfElectricCurrent.AMPERE:
            return SensorDeviceClass.CURRENT
        elif unit == UnitOfPower.WATT:
            return SensorDeviceClass.POWER
        elif unit == UnitOfEnergy.KILO_WATT_HOUR:
            return SensorDeviceClass.ENERGY
        elif unit == PERCENTAGE:
            return SensorDeviceClass.BATTERY
        return None

    @property
    def native_value(self):
        """Liefert den aktuellen Wert."""
        return self.coordinator.data.get(self._dps_code)


class DabbssonOnlineStatus(CoordinatorEntity, BinarySensorEntity):
    """Repräsentiert den Online-Status des Geräts."""

    def __init__(self, coordinator, api):
        super().__init__(coordinator)
        self.api = api
        self._attr_name = "Online-Status"
        self._attr_unique_id = f"{api.device_id}_online"
        self._attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    @property
    def is_on(self) -> bool:
        """Gibt an, ob das Gerät online ist."""
        return self.api.is_online
