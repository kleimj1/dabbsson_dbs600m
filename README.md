# Dabbsson DBS600M Integration für Home Assistant (Tuya Cloud)

Diese benutzerdefinierte Integration ermöglicht die **direkte Einbindung des Dabbsson DBS600M Wechselrichters** in Home Assistant – über die **offizielle Tuya Cloud API**. Es ist keine lokale API, kein Bluetooth und kein zusätzlicher MQTT-Server erforderlich.

---

## ✨ Funktionen

- 📊 Live-Daten auslesen: PV-Leistung, Spannung, Strom, Temperatur, Batterie-SoC u.v.m.
- 🧠 Automatische Entitätenerkennung auf Basis der Tuya-DPS
- 🔁 Steuerung: Wechselrichter EIN/AUS, Power-Limit setzen, Betriebsmodus umschalten, Zähler zurücksetzen
- 🔢 Unterstützung für Zahlenwerte und Auswahllisten
- 📡 Cloudbasiert – kein lokaler Zugriff auf das Gerät notwendig
- 🧩 Saubere Trennung von Datenmodell und Logik via `dps_metadata.py`

---

## 🚀 Installation über HACS

1. **HACS öffnen** → Integrationen
2. **Benutzerdefiniertes Repository hinzufügen**
   - URL: `https://github.com/kleimj1/dabbsson_dbs600m`
   - Typ: **Integration**
3. Integration „**Dabbsson DBS600M**“ aus der Liste installieren
4. Home Assistant neustarten
5. In Geräte & Dienste → Integration „Dabbsson DBS600M“ hinzufügen

---

## ⚙️ Einrichtung

Bei der Konfiguration über die Benutzeroberfläche werden folgende Angaben benötigt:

- **Client ID** – aus deinem Tuya IoT Cloud Projekt
- **Client Secret**
- **Device ID** – z. B. `bf9e2bbde3f9c16dfe4vdb`

Der Zugriffstoken wird automatisch abgerufen und regelmäßig erneuert.

---

## 🧪 Unterstützte Entitäten (Auszug)

### 🔍 Sensoren (`sensor.*`)

| Entität                        | Beschreibung                          |
|-------------------------------|---------------------------------------|
| `pv_power`                    | PV-Eingangsleistung (W)               |
| `pv_volt`, `pv_current`       | PV-Spannung & Strom (V, A)            |
| `temperature`, `ac_current`   | Invertertemperatur, AC-Strom          |
| `out_power`                   | AC-Ausgangsleistung (W)               |
| `bat_capacity`                | Batteriestatus (%)                    |
| `day_energy`, `energy`        | Energieverbrauch (kWh)                |
| `plant`, `emission`           | Umweltmetriken: Bäume, CO₂-Ersparnis  |

### 🔘 Schalter (`switch.*`)

| Entität                | Beschreibung                   |
|------------------------|--------------------------------|
| `switch`               | Wechselrichter EIN/AUS         |
| `clear_energy`         | Energiezähler zurücksetzen     |
| `anti_reflux_flag`     | Anti-Einspeise-Funktion        |
| `add_node`, `delete_all_nodes` | Knotensteuerung         |

### 🎚 Zahlen (`number.*`)

| Entität               | Beschreibung                   |
|------------------------|-------------------------------|
| `power_adjustment`     | Leistungsgrenze in Prozent     |
| `inv_mode_set`         | Modusparameter (INV intern)    |

### 📂 Auswahlfelder (`select.*`)

| Entität       | Beschreibung                     |
|----------------|----------------------------------|
| `workmode`     | Betriebsmodus: Eco oder Batterie |
| `power_src`    | Energiequelle (PV, Netz, Akku)   |

---

## 🔒 Datenschutz & Cloud-Zugriff

- **Reine Cloud-Kommunikation** via Tuya OpenAPI (Europa-Endpoint voreingestellt)
- **Kein lokaler Zugriff** oder Weitergabe der Daten an Dritte
- Access-Token wird automatisch verwaltet und erneuert

---

## 🗂 Verzeichnisstruktur

```text
custom_components/dabbsson_dbs600m/
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
└── translations/
    └── de.json
```

---

## 📘 Hinweise

- Die genaue Entitätsauswahl basiert auf dem Tuya-Datenmodell deines Geräts (`dps_metadata.py`)
- Die Integration kann beliebig oft hinzugefügt werden – ideal für Multi-Wechselrichter-Installationen
- Für Fragen oder Erweiterungsvorschläge gerne ein GitHub-Issue erstellen
