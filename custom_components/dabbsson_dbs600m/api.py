import time
import hashlib
import hmac
import json
import aiohttp
from .const import API_BASE_URL

class TuyaCloudAPI:
    def __init__(self, client_id, client_secret, region="eu"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.region = region
        self.api_url = f"https://openapi.tuya{region}.com"
        self.access_token = None
        self.refresh_token = None
        self.expire_time = 0

    def _get_timestamp(self):
        return str(int(time.time() * 1000))

    def _sign(self, method, path, t, access_token="", body=""):
        content = self.client_id + access_token + t + method.upper() + path + body
        signature = hmac.new(
            self.client_secret.encode("utf-8"),
            content.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest().upper()
        return signature

    def _get_headers(self, method, path, t, sign, access_token=""):
        headers = {
            "client_id": self.client_id,
            "sign": sign,
            "t": t,
            "sign_method": "HMAC-SHA256",
            "mode": "cors",
            "Content-Type": "application/json",
        }
        if access_token:
            headers["access_token"] = access_token
        return headers

    async def _ensure_token(self):
        if self.access_token and time.time() < self.expire_time:
            return

        t = self._get_timestamp()
        path = "/v1.0/token?grant_type=1"
        sign = self._sign("GET", path, t)
        headers = self._get_headers("GET", path, t, sign)
        url = f"{self.api_url}{path}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                result = await response.json()
                if not result.get("success"):
                    raise Exception(f"Token Error: {result}")
                data = result["result"]
                self.access_token = data["access_token"]
                self.refresh_token = data["refresh_token"]
                self.expire_time = time.time() + data["expire_time"] - 60

    async def get_device_properties(self, device_id):
        await self._ensure_token()
        t = self._get_timestamp()
        path = f"/v2.0/cloud/thing/{device_id}/shadow/properties"
        body = ""
        sign = self._sign("GET", path, t, self.access_token, body)
        headers = self._get_headers("GET", path, t, sign, self.access_token)
        url = f"{self.api_url}{path}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                result = await response.json()
                if not result.get("success"):
                    raise Exception(f"Get properties failed: {result}")
                return result.get("result", {}).get("properties", [])

    async def set_device_property(self, device_id, code, value):
        await self._ensure_token()
        path = f"/v2.0/cloud/thing/{device_id}/shadow/properties/issue"
        url = f"{self.api_url}{path}"
        body_data = {"properties": json.dumps({code: value})}
        body_str = json.dumps(body_data)
        t = self._get_timestamp()
        sign = self._sign("POST", path, t, self.access_token, body_str)
        headers = self._get_headers("POST", path, t, sign, self.access_token)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=body_data) as response:
                result = await response.json()
                if not result.get("success"):
                    raise Exception(f"Set property failed: {result}")
                return True
