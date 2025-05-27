Kategorie: **Integration**
4. Nach dem Hinzufügen die Integration wie gewohnt einrichten:
- → Einstellungen
- → Geräte & Dienste
- → Integration hinzufügen: **Dabbsson DBS600M**

---

## ⚙️ Konfiguration

Nach dem Start wirst du nach den folgenden Werten gefragt:

- `Client ID` (aus Tuya Cloud Projekt)
- `Client Secret`
- `Access Token`
- `Device ID` (z. B. `bf9e2bbde3f9c16dfe4vdb`)

---

## 🧪 Unterstützte Entitäten

### Sensoren
| Entität                        | Beschreibung                     |
|-------------------------------|----------------------------------|
| `sensor.dbs600m_pv_leistung`  | PV-Leistung in Watt              |
| `sensor.dbs600m_pv_spannung`  | PV-Spannung in Volt              |
| `sensor.dbs600m_pv_strom`     | PV-Strom in Ampere               |
| `sensor.dbs600m_inverter_temp`| Temperatur des Wechselrichters   |
| `sensor.dbs600m_ac_leistung`  | AC-Ausgangsleistung              |
| `sensor.dbs600m_batterie_soc` | Ladezustand der Batterie (%)     |

### Schalter
| Entität                         | Funktion                     |
|--------------------------------|------------------------------|
| `switch.dbs600m_inverter`      | Wechselrichter EIN/AUS       |
| `switch.dbs600m_reset_energy`  | Energiezähler zurücksetzen   |

### Zahleneingabe
| Entität                           | Beschreibung                  |
|----------------------------------|-------------------------------|
| `number.dbs600m_power_limit`     | Leistungslimit in %          |

### Auswahlfeld
| Entität                          | Beschreibung                  |
|----------------------------------|-------------------------------|
| `select.dbs600m_arbeitsmodus`   | Eco-Modus oder Batteriebetrieb|

---

## 🔐 Datenschutz

Diese Integration verwendet ausschließlich die **offizielle Tuya Cloud API**. Es werden keine Daten an Dritte weitergeleitet.

---

## 📄 Lizenz

MIT License
