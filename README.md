# 🧠 Dabbsson DBS600M Integration (Tuya via WLAN)

Diese benutzerdefinierte Integration ermöglicht die Einbindung des **Dabbsson DBS600M** direkt über das **lokale Tuya-Protokoll via WLAN**. Die Kommunikation erfolgt per `tinytuya`, ohne Cloud oder Bluetooth.

---

## ✅ Funktionen

- 🔌 Verbindung über WLAN (lokales Tuya-Protokoll)  
- 🔄 Automatische Erstellung von Sensoren & Schaltern  
- 🖥️ Schreibzugriff auf unterstützte DPS-Werte  
- 🔒 Keine Cloud notwendig  
- 💬 Unterstützt Deutsch und Englisch

---

## 🚀 Installation über HACS

Diese Integration ist mit [HACS (Home Assistant Community Store)](https://hacs.xyz) kompatibel.

### Schritt-für-Schritt

1. Öffne Home Assistant → HACS → Integrationen  
2. Klick auf „Benutzerdefinierte Repositories hinzufügen“  
3. Repository-URL:

```
https://github.com/kleimj1/dabbsson_dbs600m
```

4. Kategorie: `Integration`  
5. Danach: Integration wie gewohnt über `Einstellungen → Geräte & Dienste → Integration hinzufügen` einrichten

---

## ⚙️ Konfiguration

Die Integration wird über den Home Assistant UI Konfigurationsdialog eingerichtet.

Du brauchst:

- 📦 `Device ID`  
- 🔑 `Local Key`  
- 🌐 Lokale IP-Adresse des Geräts (z. B. `192.168.178.30`)

---

## 🧪 Unterstützte Entitäten

### Sensoren

- `sensor.dbs600m_pv_leistung` – PV-Leistung (W)  
- `sensor.dbs600m_pv_spannung` – PV-Spannung (V)  
- `sensor.dbs600m_pv_strom` – PV-Strom (A)  
- `sensor.dbs600m_inverter_temp` – Temperatur des Wechselrichters (°C)  
- `sensor.dbs600m_ac_ausgang_leistung` – AC Ausgangsleistung (W)  
- `sensor.dbs600m_batterie_soc` – Batterie-SoC (%)

### Schalter / Steuerung

- `switch.dbs600m_wechselrichter` – Wechselrichter EIN/AUS  
- `switch.dbs600m_zaehler_zuruecksetzen` – Energiezähler zurücksetzen  
- `number.dbs600m_power_limit` – Ausgangsleistungsbegrenzung (%)  
- `select.dbs600m_arbeitsmodus` – Arbeitsmodus (Eco / Ladung)

---

## 🔒 Datenschutz

Die Integration arbeitet vollständig lokal. Es werden keine Daten an Cloud-Dienste übertragen.
