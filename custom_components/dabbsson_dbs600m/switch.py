from homeassistant.components.switch import SwitchEntity
from .api import get_device_properties, set_device_property
from .const import DOMAIN
from .dps_metadata import DPS_METADATA

async def async_setup_entry(hass, config_entry, async_add_entities):
    device_id = config_entry.data["device_id"]
    headers = config_entry.data["headers"]
    data = get_device_properties(device_id, headers)
    switches = [DabbssonSwitch(dp, device_id, headers) for dp in data if dp["code"] in DPS_METADATA and DPS_METADATA[dp["code"]]["type"] == "bool" and DPS_METADATA[dp["code"]].get("writable")]
    async_add_entities(switches, True)

class DabbssonSwitch(SwitchEntity):
    def __init__(self, dp, device_id, headers):
        self._device_id = device_id
        self._headers = headers
        self._code = dp.get("code")
        self._value = dp.get("value")
        self._attr_name = DPS_METADATA[self._code].get("name", self._code)
        self._attr_unique_id = f"dbs600m_{dp.get('dp_id')}"

    @property
    def is_on(self):
        return self._value is True

    def turn_on(self, **kwargs):
        set_device_property(self._device_id, self._headers, self._code, True)
        self._value = True

    def turn_off(self, **kwargs):
        set_device_property(self._device_id, self._headers, self._code, False)
        self._value = False
