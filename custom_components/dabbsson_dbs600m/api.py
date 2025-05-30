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
    DATA_DEVICE,
)

_LOGGER = logging.getLogger(__name__)


class TuyaDeviceApi:
    """API Wrapper für Tuya Wechselrichter."""

    def __init__(self, client_id: str, client_secret: str, device_id: str, api_endpoint: str):
        self.device_id = device_id
        self._openapi = TuyaOpenAPI(api_endpoint, client_id, client_secret)
        self._connected = False
        self.is_online = True  # Standardmäßig als online behandeln

    async def connect(self) -> bool:
        """Verbindet zur Tuya Cloud API (async-safe)."""
        try:
            await asyncio.to_thread(self._openapi.connect)
            self._connected = True
            _LOGGER.debug("Verbindung zur Tuya Cloud erfolgreich.")
            return True
        except Exception as err:
            _LOGGER.warning("Fehler bei Tuya-API-Verbindung: %s", err)
            return False

    async def get_status(self) -> dict[str, Any]:
        """Liefert Gerätestatus."""
        # Online-Status parallel mitlesen
        await self._update_online_status()

        response = await asyncio.to_thread(
            self._openapi.get, f"/v1.0/iot-03/devices/{self.device_id}/status"
        )
        if response.get("success"):
            return {item["code"]: item["value"] for item in response.get("result", [])}
        raise Exception(f"Fehler beim Abrufen des Gerätestatus: {response}")

    async def send_command(self, code: str, value: Any) -> bool:
        """Sendet einen Steuerbefehl an das Gerät."""
        if not self.is_online:
            _LOGGER.warning("⚠️ Gerät ist offline – Befehle werden nicht gesendet: %s = %s", code, value)
            return False

        commands = {"commands": [{"code": code, "value": value}]}
        response = await asyncio.to_thread(
            self._openapi.post, f"/v1.0/iot-03/devices/{self.device_id}/commands", commands
        )
        success = response.get("success", False)
        if not success:
            _LOGGER.warning("Senden des Befehls %s = %s fehlgeschlagen: %s", code, value, response)
        return success

    async def _update_online_status(self):
        """Fragt den Online-Status des Geräts ab und speichert ihn."""
        try:
            response = await asyncio.to_thread(
                self._openapi.get, f"/v2.0/cloud/thing/batch?device_ids={self.device_id}"
            )
            info = response.get("result", [{}])[0]
            self.is_online = info.get("is_online", False)
            _LOGGER.debug("📶 Gerätestatus (online): %s", self.is_online)
        except Exception as err:
            _LOGGER.warning("Konnte Online-Status nicht abrufen: %s", err)
            self.is_online = True  # Fallback: nicht blockieren
