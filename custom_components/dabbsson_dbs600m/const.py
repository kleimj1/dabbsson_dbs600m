"""Konstanten für die Dabbsson DBS600M Integration."""

DOMAIN = "dabbsson_dbs600m"
PLATFORMS = ["sensor", "number", "select", "switch"]

# Konfigurationsschlüssel
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CONF_DEVICE_ID = "device_id"
CONF_API_ENDPOINT = "api_endpoint"
CONF_NAME = "name"

# Standardwerte
DEFAULT_API_ENDPOINT = "https://openapi.tuyaeu.com"

# Gemeinsame Datenablagen
DATA_COORDINATOR = "coordinator"
DATA_DEVICE = "device"

# Version
INTEGRATION_VERSION = "2.1.6"
