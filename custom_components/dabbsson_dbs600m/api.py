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
    """API Wrapper für Tuya Wechselrichter mit optimiertem Token- & Statushandling."""

    def __init__(self, client_id: str, client_secret: str, device_id: str, api_endpoint: str):
        self.device_id = device_id
        self._openapi = TuyaOpenAPI(api_endpoint, client_id, client_secret)
        self._connected = False
        self.is_online = True

        self._last_online_check = 0
        self._online_check_interval = 1800  # alle 30 Minuten

    async def connect(self) -> bool:
        """Initialer API-Connect. Kein reconnect bei jedem Aufruf."""
        if not self._connected:
            try:
                await asyncio.to_thread(self._openapi.connect)
                self._connected = True
                _LOGGER.info("✅ Verbindung zur Tuya Cloud erfolgreich.")
                return True
            except Exception as err:
                _LOGGER.error("❌ Fehler bei Tuya-API-Verbindung: %s", err)
                return False
        return True

    async def get_status(self) -> dict[str, Any]:
        """Liefert Gerätestatus. Führt ggf. seltenen Online-Check durch."""
        await self._maybe_update_online_status()

        try:
            response = await asyncio.to_thread(
                self._openapi.get, f"/v1.0/iot-03/devices/{self.device_id}/status"
            )
            if response.get("success"):
                status = {item["code"]: item["value"] for item in response.get("result", [])}
                _LOGGER.debug("📟 Gerätestatus erhalten: %s", status)
                return status
            raise Exception(f"Tuya Fehlerantwort: {response}")
        except Exception as err:
            _LOGGER.error("❌ Fehler beim Statusabruf: %s", err)
            raise

    async def send_command(self, code: str, value: Any) -> bool:
        """Sendet einen Steuerbefehl, wenn Gerät online."""
        if not self.is_online:
            _LOGGER.warning("⚠️ Gerät offline – Befehl verworfen (%s = %s)", code, value)
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
                _LOGGER.warning("❌ Befehl fehlgeschlagen (%s = %s): %s", code, value, response)
            return success
        except Exception as err:
            _LOGGER.error("❌ Ausnahme beim Befehl (%s = %s): %s", code, value, err)
            return False

    async def _maybe_update_online_status(self):
        """Führt Online-Check nur alle 30 Minuten durch."""
        now = time.time()
        if now - self._last_online_check < self._online_check_interval:
            return

        try:
            response = await asyncio.to_thread(
                self._openapi.get, f"/v2.0/cloud/thing/batch?device_ids={self.device_id}"
            )
            result = response.get("result", [{}])[0]
            self.is_online = result.get("is_online", False)
            self._last_online_check = now
            _LOGGER.info("📶 Gerätestatus: %s", "Online" if self.is_online else "Offline")
        except Exception as err:
            _LOGGER.warning("⚠️ Online-Status nicht abrufbar: %s", err)
            self.is_online = True  # Fallback


class DabbssonCoordinator(DataUpdateCoordinator):
    """Koordiniert periodischen Datenabruf vom Wechselrichter."""

    def __init__(self, hass: HomeAssistant, api: TuyaDeviceApi, name: str):
        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=timedelta(minutes=5),  # 🕒 Jetzt: nur alle 5 Minuten!
        )
        self.api = api

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            return await self.api.get_status()
        except Exception as err:
            raise UpdateFailed(f"❌ Fehler beim Tuya-Datenabruf: {err}") from err
