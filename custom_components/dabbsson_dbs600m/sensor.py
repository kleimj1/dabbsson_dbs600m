from homeassistant.components.sensor import SensorEntity
from .api import get_device_properties
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    device_id = config_entry.data["device_id"]
    headers = config_entry.data["headers"]
    data = get_device_properties(device_id, headers)
    sensors = [DabbssonSensor(dp) for dp in data if dp["type"] == "value"]
    async_add_entities(sensors, True)

class DabbssonSensor(SensorEntity):
    def __init__(self, dp):
        self._attr_name = dp.get("code")
        self._attr_unique_id = f"dbs600m_{dp.get('dp_id')}"
        self._dp_id = dp.get("dp_id")
        self._code = dp.get("code")
        self._unit = dp.get("unit", "")
        self._value = dp.get("value")

    @property
    def native_value(self):
        return self._value

    def update(self):
        properties = get_device_properties(self._dp_id)
        for dp in properties:
            if dp.get("dp_id") == self._dp_id:
                self._value = dp.get("value")
