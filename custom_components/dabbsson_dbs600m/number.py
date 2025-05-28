from homeassistant.components.number import NumberEntity
from .api import TuyaCloudAPI
from .const import DOMAIN
from .dps_metadata import DPS_METADATA

async def async_setup_entry(hass, config_entry, async_add_entities):
    client_id = config_entry.data["client_id"]
    client_secret = config_entry.data["client_secret"]
    device_id = config_entry.data["device_id"]

    api = TuyaCloudAPI(client_id, client_secret)
    data = api.get_device_properties(device_id)

    numbers = [
        DabbssonNumber(dp, api, device_id)
        for dp in data
        if dp["code"] in DPS_METADATA
        and DPS_METADATA[dp["code"]]["type"] == "value"
        and DPS_METADATA[dp["code"]].get("writable")
    ]
    async_add_entities(numbers, True)

class DabbssonNumber(NumberEntity):
    def __init__(self, dp, api, device_id):
        self._device_id = device_id
        self._api = api
        self._code = dp.get("code")
        self._value = dp.get("value")
        meta = DPS_METADATA[self._code]
        self._attr_name = meta.get("name", self._code)
        self._attr_unique_id = f"dbs600m_{dp.get('dp_id')}"
        self._attr_unit_of_measurement = meta.get("unit")
        self._attr_native_min_value = meta.get("min", 0)
        self._attr_native_max_value = meta.get("max", 100)
        self._attr_native_step = meta.get("step", 1)

    @property
    def native_value(self):
        return self._value

    def set_native_value(self, value):
        success = self._api.set_device_property(self._device_id, self._code, value)
        if success:
            self._value = value
