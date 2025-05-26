from homeassistant.components.sensor import SensorEntity
from homeassistant.const import (
    PERCENTAGE,
    POWER_WATT,
    VOLT,
    TEMP_CELSIUS,
    ELECTRIC_CURRENT_AMPERE
)
from .const import DOMAIN, DEFAULT_NAME

SENSOR_TYPES = {
    "101": ("pv_leistung", "PV-Leistung", POWER_WATT, "power"),
    "103": ("pv_spannung", "PV-Spannung", VOLT, "voltage"),
    "104": ("inverter_temp", "Inverter-Temp", TEMP_CELSIUS, "temperature"),
    "109": ("ac_ausgang_leistung", "AC Ausgang Leistung", POWER_WATT, "power"),
    "111": ("pv_strom", "PV-Strom", ELECTRIC_CURRENT_AMPERE, "current"),
    "120": ("batterie_soc", "Batterie SoC", PERCENTAGE, "battery"),
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    device = hass.data[DOMAIN][config_entry.entry_id]
    entities = []

    for dps_id, (key, name, unit, device_class) in SENSOR_TYPES.items():
        if dps_id in device.status:
            entities.append(DabbssonSensor(device, dps_id, key, name, unit, device_class))

    async_add_entities(entities)


class DabbssonSensor(SensorEntity):
    def __init__(self, device, dps_id, key, name, unit, device_class):
        self._device = device
        self._dps_id = dps_id
        self._attr_name = f"{DEFAULT_NAME} {name}"
        self._attr_unique_id = f"{device.id}_{key}"
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class

    @property
    def native_value(self):
        return self._device.status.get(self._dps_id)
