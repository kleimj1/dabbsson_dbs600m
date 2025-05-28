# Dabbsson DBS600M Integration für Home Assistant (Tuya Cloud)

Diese benutzerdefinierte Integration ermöglicht die direkte Einbindung des Dabbsson DBS600M Wechselrichters über die **offizielle Tuya Cloud API** in Home Assistant – ohne lokale API oder Bluetooth.

---

## ✨ Features

- 🌩️ Live-Daten über PV-Leistung, Stromstärke, Temperatur, BatteriesoC etc.
- 🔁 Steuerung: Wechselrichter EIN/AUS, Power-Limit setzen, Zähler zurücksetzen
- 🧮 Zahleneingaben & Auswahllisten (Moduswahl, Leistungsgrenzen etc.)
- 📡 Cloud-Zugriff (kein lokaler Netzwerkzugriff erforderlich)
- 🧠 Automatische Entitätenerkennung auf Basis des Tuya Datenmodells
- 📑 DPS-Mapping vollständig in `dps_metadata.py` definiert

---

## 🚀 Installation via HACS

1. Öffne Home Assistant → HACS → Integrationen
2. Klicke auf „Benutzerdefiniertes Repository hinzufügen“
   - URL: `https://github.com/kleimj1/dabbsson_dbs600m`
   - Kategorie: **Integration**
3. Suche unter Geräte & Dienste nach „**Dabbsson DBS600M**“ und richte die Integration ein

---

## ⚙️ Konfiguration

Bei der Einrichtung wirst du nach folgenden Daten gefragt:

- `Client ID` – aus deinem Tuya IoT Cloud-Projekt
- `Client Secret`
- `Device ID` – z. B. `bf9e2bbde3f9c16dfe4vdb`

Das Access Token wird automatisch über die API geholt und bei Bedarf erneuert.

---

## 🧪 Unterstützte Entitäten (Auszug)

### Sensoren (`sensor.*`)

| Entität                              | Beschreibung                        |
|-------------------------------------|-------------------------------------|
| `pv_power`                          | PV-Eingangsleistung (W)             |
| `pv_volt`                           | PV-Spannung (V)                     |
| `pv_current`                        | PV-Strom (A)                        |
| `temperature`                       | Inverter-Temperatur (°C)            |
| `ac_current`                        | AC-Strom (A)                        |
| `out_power`                         | AC-Ausgangsleistung (W)             |
| `bat_capacity`                      | Batteriekapazität (%)               |
| `day_energy`, `energy`, `total_power` | Energie-Statistiken (kWh)           |
| `plant`                             | Virtuell gepflanzte Bäume (pcs)     |
| `emission`                          | CO2-Einsparung (kg)                 |
| u.v.m. (siehe `dps_metadata.py`)    |                                     |

### Schalter (`switch.*`)

| Entität                     | Beschreibung                         |
|----------------------------|--------------------------------------|
| `switch`                   | Wechselrichter EIN/AUS               |
| `clear_energy`             | Zähler zurücksetzen                  |
| `anti_reflux_flag`         | Anti-Feed-In-Funktion                |
| `add_node`, `delete_all_nodes` | Knotenmanagement                     |

### Zahlen (`number.*`)

| Entität                   | Beschreibung                          |
|--------------------------|---------------------------------------|
| `power_adjustment`       | Leistungsgrenze in %                  |
| `inv_mode_set`           | INV Modus Parameter                   |

### Auswahlfelder (`select.*`)

| Entität         | Beschreibung                    |
|----------------|---------------------------------|
| `workmode`     | Eco- oder Batteriebetrieb       |
| `pv_to_bat`    | Ladevorgang aktiv (enum)        |
| `power_src`    | Eingangsquelle (enum)           |

---

## 🔒 Datenschutz

Diese Integration kommuniziert **ausschließlich mit der Tuya Cloud API**. Es werden keine Daten an Dritte weitergegeben oder lokal zwischengespeichert. Das Access Token wird automatisch verwaltet.

---

## 🧱 Struktur

```text
custom_components/dbs600m/
├── __init__.py
├── api.py
├── const.py
├── config_flow.py
├── dps_metadata.py
├── manifest.json
├── sensor.py
├── switch.py
├── number.py
├── select.py
├── translations/
│   └── de.json
