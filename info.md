# Dabbsson DBS600M Integration

Integration zur Anbindung des Wechselrichters **Dabbsson DBS600M** über die **Tuya Cloud API**.

## 🔧 Funktionen

- Unterstützt mehrere Geräteinstanzen
- Zeigt aktuelle Statuswerte (Sensoren)
- Ermöglicht Steuerung über Schalter, Regler, Auswahlmenüs
- Verbindung über `tuya-connector-python`

## 🛠 Konfiguration

Die Konfiguration erfolgt vollständig über das UI. Du benötigst:

- Tuya **Client ID** & **Client Secret**
- Die **Device ID** des Geräts (z. B. aus der Tuya IoT Cloud Console)

## 💡 Unterstützte Entitäten

- `sensor` (z. B. Temperatur, Spannung, Leistung)
- `switch` (z. B. Wechselrichter EIN/AUS)
- `number` (z. B. Leistungsbegrenzung)
- `select` (z. B. Arbeitsmodus wählen)

## 🗺 API-Region

Standardmäßig wird Tuya Europe verwendet (`https://openapi.tuyaeu.com`). Optional kannst du einen anderen Endpunkt wählen.

## 📦 Abhängigkeiten

- `tuya-connector-python`
