import time
import hashlib
import hmac
import requests
import json
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

    def _get_headers(self, method, path, access_token="", body=""):
        t = self._get_timestamp()
        body_str = json.dumps(body) if body else ""
        sign = self._sign(method, path, t, access_token, body_str)
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

    def _ensure_token(self):
        if self.access_token and time.time() < self.expire_time:
            return

        # Fetch new token
        url = f"{self.api_url}/v1.0/token?grant_type=1"
        headers = self._get_headers("GET", "/v1.0/token?grant_type=1")
        response = requests.get(url, headers=headers)

        if response.ok:
            data = response.json()["result"]
            self.access_token = data["access_token"]
            self.refresh_token = data["refresh_token"]
            self.expire_time = time.time() + data["expire_time"] - 60
        else:
            raise Exception(f"Failed to get token: {response.text}")

    def get_device_properties(self, device_id):
        self._ensure_token()
        path = f"/v2.0/cloud/thing/{device_id}/shadow/properties"
        url = f"{self.api_url}{path}"
        headers = self._get_headers("GET", path, self.access_token)
        response = requests.get(url, headers=headers)
        if response.ok:
            return response.json().get("result", {}).get("properties", [])
        return []

    def set_device_property(self, device_id, code, value):
        self._ensure_token()
        path = f"/v2.0/cloud/thing/{device_id}/shadow/properties/issue"
        url = f"{self.api_url}{path}"
        body = {"properties": json.dumps({code: value})}
        headers = self._get_headers("POST", path, self.access_token, body)
        response = requests.post(url, headers=headers, json=body)
        return response.ok
