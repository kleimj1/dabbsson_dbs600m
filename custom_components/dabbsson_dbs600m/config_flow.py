from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_CLIENT_ID, CONF_CLIENT_SECRET, CONF_ACCESS_TOKEN, CONF_DEVICE_ID
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

class DabbssonConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="DBS600M", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_CLIENT_ID): str,
                vol.Required(CONF_CLIENT_SECRET): str,
                vol.Required(CONF_DEVICE_ID): str,
            })
        )
