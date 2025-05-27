from homeassistant.components.select import SelectEntity
from .api import get_device_properties, set_device_property
from .const import DOMAIN
from .dps_metadata import DPS_METADATA

async def async_setup_entry(hass, config_entry, async_add_entities):
    device_id = config_entry.data["device_id"]
    headers = config_entry.data["headers"]
    data = get_device_properties(device_id, headers)
    selects = [DabbssonSelect(dp, device_id, headers) for dp in data if dp["code"] in DPS_METADATA and DPS_METADATA[dp["code"]]["type"] == "enum"]
    async_add_entities(selects, True)

class DabbssonSelect(SelectEntity):
    def __init__(self, dp, device_id, headers):
        self._device_id = device_id
        self._headers = headers
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
        set_device_property(self._device_id, self._headers, self._code, option)
        self._value = option
