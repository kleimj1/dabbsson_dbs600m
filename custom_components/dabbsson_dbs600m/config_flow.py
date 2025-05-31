from __future__ import annotations

import asyncio
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN,
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    CONF_DEVICE_ID,
    CONF_NAME,
    CONF_API_ENDPOINT,
    DEFAULT_API_ENDPOINT,
)

from .api import TuyaDeviceApi

_LOGGER = logging.getLogger(__name__)


class DabbssonDBS600MConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dabbsson DBS600M."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        self._data: dict = {}

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        errors = {}

        if user_input is not None:
            client_id = user_input[CONF_CLIENT_ID]
            client_secret = user_input[CONF_CLIENT_SECRET]
            device_id = user_input[CONF_DEVICE_ID]
            api_endpoint = user_input.get(CONF_API_ENDPOINT, DEFAULT_API_ENDPOINT)
            name = user_input[CONF_NAME]

            if await self._validate_tuya_credentials(client_id, client_secret, api_endpoint, device_id):
                await self.async_set_unique_id(device_id)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=name,
                    data={
                        CONF_CLIENT_ID: client_id,
                        CONF_CLIENT_SECRET: client_secret,
                        CONF_DEVICE_ID: device_id,
                        CONF_API_ENDPOINT: api_endpoint,
                        CONF_NAME: name,
                    },
                )
            else:
                errors["base"] = "auth_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_CLIENT_ID): str,
                vol.Required(CONF_CLIENT_SECRET): str,
                vol.Required(CONF_DEVICE_ID): str,
                vol.Optional(CONF_API_ENDPOINT, default=DEFAULT_API_ENDPOINT): str,
                vol.Required(CONF_NAME, default="Dabbsson DBS600M"): str,
            }),
            errors=errors,
        )

    async def _validate_tuya_credentials(self, client_id: str, client_secret: str, api_endpoint: str, device_id: str) -> bool:
        """Testet Tuya API Verbindung mit den angegebenen Anmeldedaten."""
        try:
            api = TuyaDeviceApi(client_id, client_secret, device_id, api_endpoint)
            if not await api.connect():
                return False

            status = await api.get_status()
            _LOGGER.debug("✅ Tuya-Anmeldedaten erfolgreich validiert. Status: %s", status)
            return True
        except Exception as err:
            _LOGGER.warning("❌ Validierung der Tuya-Anmeldedaten fehlgeschlagen: %s", err)
            return False

    @staticmethod
    @callback
    def async_get_options_flow(entry: config_entries.ConfigEntry):
        return DabbssonDBS600MOptionsFlowHandler(entry)


class DabbssonDBS600MOptionsFlowHandler(config_entries.OptionsFlow):
    """Optionen für die Integration – später erweiterbar."""

    def __init__(self, entry: config_entries.ConfigEntry) -> None:
        self.config_entry = entry

    async def async_step_init(self, user_input=None) -> FlowResult:
        return self.async_create_entry(title="", data={})
