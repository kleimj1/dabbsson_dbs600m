import requests
from .const import API_BASE_URL

def get_device_properties(device_id, headers):
    url = f"{API_BASE_URL}/v2.0/cloud/thing/{device_id}/shadow/properties"
    resp = requests.get(url, headers=headers)
    if resp.ok:
        return resp.json().get("result", {}).get("properties", [])
    return []
