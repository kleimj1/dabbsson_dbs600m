import logging
import asyncio
import time
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
    """API Wrapper für Tuya Wechselrichter mit Token-Caching."""

    def __init__(self, client_id: str, client_secret: str, device_id: str, api_endpoint: str):
        self.device_id = device_id
        self._openapi = TuyaOpenAPI(api_endpoint, client_id, client_secret)
        self._connected = False
        self.is_online = True
        self._token_expiry = 0  # Millisekunden-Zeitstempel

    async def connect(self) -> bool:
        """Verbindet zur Tuya Cloud API mit Token-Caching."""
        now = int(time.time() * 1000)
        if self._connected and now < self._token_expiry:
            _LOGGER.debug("🔁 Bestehende Tuya-Verbindung wird wiederverwendet.")
            return True

        try:
            await asyncio.to_thread(self._openapi.connect)
            self._connected = True
            self._token_expiry = now + 3500 * 1000  # konservative 58 Minuten statt 1h
            _LOGGER.info("✅ Neue Verbindung zur Tuya Cloud erfolgreich aufgebaut.")
            return True
        except Exception as err:
            _LOGGER.error("❌ Fehler bei Tuya-API-Verbindung: %s", err)
            self._connected = False
            return False

    async def get_status(self) -> dict[str, Any]:
        """Liefert Gerätestatus und prüft Online-Verfügbarkeit."""
        await self.connect()
        await self._update_online_status()

        try:
            response = await asyncio.to_thread(
                self._openapi.get, f"/v1.0/iot-03/devices/{self.device_id}/status"
            )
            if response.get("success"):
                status = {item["code"]: item["value"] for item in response.get("result", [])}
                _LOGGER.debug("📟 Gerätestatus erhalten: %s", status)
                return status
            raise Exception(f"Tuya antwortete mit Fehler: {response}")
        except Exception as err:
            _LOGGER.error("❌ Fehler beim Abrufen des Gerätestatus: %s", err)
            raise

    async def send_command(self, code: str, value: Any) -> bool:
        """Sendet einen Steuerbefehl an das Gerät."""
        await self.connect()
        if not self.is_online:
            _LOGGER.warning("⚠️ Gerät offline – Befehl nicht gesendet (%s = %s)", code, value)
            return False

        commands = {"commands": [{"code": code, "value": value}]}
        try:
            response = await asyncio.to_thread(
                self._openapi.post, f"/v1.0/iot-03/devices/{self.device_id}/commands", commands
            )
            success = response.get("success", False)
            if success:
                _LOGGER.info("✅ Befehl gesendet: %s = %s", code, value)
            else:
                _LOGGER.warning("❌ Senden des Befehls %s = %s fehlgeschlagen: %s", code, value, response)
            return success
        except Exception as err:
            _LOGGER.error("❌ Ausnahme beim Senden des Befehls (%s = %s): %s", code, value, err)
            return False

    async def _update_online_status(self):
        """Fragt den Online-Status des Geräts ab und aktualisiert ihn."""
        try:
            response = await asyncio.to_thread(
                self._openapi.get, f"/v2.0/cloud/thing/batch?device_ids={self.device_id}"
            )
            result = response.get("result", [{}])[0]
            self.is_online = result.get("is_online", False)
            _LOGGER.info("📶 Online-Status des Geräts: %s", "Online" if self.is_online else "Offline")
        except Exception as err:
            _LOGGER.warning("⚠️ Konnte Online-Status nicht ermitteln: %s", err)
            self.is_online = True


class DabbssonCoordinator(DataUpdateCoordinator):
    """Koordiniert Updates für den Wechselrichter."""

    def __init__(self, hass: HomeAssistant, api: TuyaDeviceApi, name: str):
        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=timedelta(seconds=30),
        )
        self.api = api

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            return await self.api.get_status()
        except Exception as err:
            raise UpdateFailed(f"❌ Fehler beim Tuya-Datenabruf: {err}") from err
