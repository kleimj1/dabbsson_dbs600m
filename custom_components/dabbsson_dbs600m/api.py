import logging
import asyncio
from datetime import timedelta
from typing import Any

from tuya_connector import TuyaOpenAPI

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    DOMAIN,
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    CONF_DEVICE_ID,
    CONF_API_ENDPOINT,
    DATA_COORDINATOR,
)

_LOGGER = logging.getLogger(__name__)


class TuyaDeviceApi:
    """API Wrapper für Tuya Wechselrichter."""

    def __init__(self, client_id: str, client_secret: str, device_id: str, api_endpoint: str):
        self.device_id = device_id
        self._openapi = TuyaOpenAPI(api_endpoint, client_id, client_secret)
        self._connected = False

    def connect(self) -> bool:
        """Verbindet zur Tuya Cloud API."""
        try:
            self._openapi.connect()
            self._connected = True
            _LOGGER.debug("Verbindung zur Tuya Cloud erfolgreich.")
            return True
        except Exception as err:
            _LOGGER.warning("Fehler bei Tuya-API-Verbindung: %s", err)
            return False

    def get_status(self) -> dict[str, Any]:
        """Liefert Gerätestatus."""
        response = self._openapi.get(f"/v1.0/iot-03/devices/{self.device_id}/status")
        if response.get("success"):
            return {item["code"]: item["value"] for item in response.get("result", [])}
        raise Exception(f"Fehler beim Abrufen des Gerätestatus: {response}")

    def send_command(self, code: str, value: Any) -> bool:
        """Sendet einen Steuerbefehl an das Gerät."""
        commands = {"commands": [{"code": code, "value": value}]}
        response = self._openapi.post(f"/v1.0/iot-03/devices/{self.device_id}/commands", commands)
        success = response.get("success", False)
        if not success:
            _LOGGER.warning("Senden des Befehls %s = %s fehlgeschlagen: %s", code, value, response)
        return success


class DabbssonCoordinator(DataUpdateCoordinator):
    """Koordiniert Updates für den Wechselrichter."""

    def __init__(self, hass: HomeAssistant, api: TuyaDeviceApi, name: str):
        """Initialisierung."""
        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=timedelta(seconds=30),
        )
        self.api = api

    async def _async_update_data(self) -> dict[str, Any]:
        """Abfrage von Daten bei Tuya."""
        try:
            return await asyncio.to_thread(self.api.get_status)
        except Exception as err:
            raise UpdateFailed(f"Fehler beim Tuya-Datenabruf: {err}") from err
