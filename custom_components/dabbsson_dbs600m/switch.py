from homeassistant.components.switch import SwitchEntity
from .api import TuyaCloudAPI
from .const import DOMAIN
from .dps_metadata import DPS_METADATA

async def async_setup_entry(hass, config_entry, async_add_entities):
    client_id = config_entry.data["client_id"]
    client_secret = config_entry.data["client_secret"]
    device_id = config_entry.data["device_id"]

    api = TuyaCloudAPI(client_id, client_secret)
    data = api.get_device_properties(device_id)

    switches = [
        DabbssonSwitch(dp, api, device_id)
        for dp in data
        if dp["code"] in DPS_METADATA
        and DPS_METADATA[dp["code"]]["type"] == "bool"
        and DPS_METADATA[dp["code"]].get("writable")
    ]
    async_add_entities(switches, True)

class DabbssonSwitch(SwitchEntity):
    def __init__(self, dp, api, device_id):
        self._device_id = device_id
        self._api = api
        self._code = dp.get("code")
        self._value = dp.get("value")
        self._attr_name = DPS_METADATA[self._code].get("name", self._code)
        self._attr_unique_id = f"dbs600m_{dp.get('dp_id')}"

    @property
    def is_on(self):
        return self._value is True

    def turn_on(self, **kwargs):
        success = self._api.set_device_property(self._device_id, self._code, True)
        if success:
            self._value = True

    def turn_off(self, **kwargs):
        success = self._api.set_device_property(self._device_id, self._code, False)
        if success:
            self._value = False
