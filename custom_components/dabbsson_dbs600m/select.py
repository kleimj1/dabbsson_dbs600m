from homeassistant.components.select import SelectEntity
from .api import TuyaCloudAPI
from .const import DOMAIN
from .dps_metadata import DPS_METADATA

async def async_setup_entry(hass, config_entry, async_add_entities):
    client_id = config_entry.data["client_id"]
    client_secret = config_entry.data["client_secret"]
    device_id = config_entry.data["device_id"]

    api = TuyaCloudAPI(client_id, client_secret)
    data = await api.get_device_properties(device_id)

    selects = [
        DabbssonSelect(dp, api, device_id)
        for dp in data
        if dp["code"] in DPS_METADATA and DPS_METADATA[dp["code"]]["type"] == "enum"
    ]
    async_add_entities(selects, True)

class DabbssonSelect(SelectEntity):
    def __init__(self, dp, api, device_id):
        self._device_id = device_id
        self._api = api
        self._code = dp.get("code")
        self._value = dp.get("value")
        meta = DPS_METADATA[self._code]
        self._attr_name = meta.get("name", self._code)
        self._attr_unique_id = f"dbs600m_{dp.get('dp_id')}"
        self._attr_options = meta.get("options", [])

    @property
    def current_option(self):
        return self._value

    def select_option(self, option):
        success = self._api.set_device_property(self._device_id, self._code, option)
        if success:
            self._value = option
