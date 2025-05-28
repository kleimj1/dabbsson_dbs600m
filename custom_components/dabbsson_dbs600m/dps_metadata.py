DPS_METADATA = {
    "1": {
        "name": "Gesamtverbrauch (kWh)",
        "type": "value",
        "writable": true,
        "description": "Gesamtverbrauch (kWh)",
        "unit": "kW·h"
    },
    "3": {
        "name": "PV1 Parameter",
        "type": "raw",
        "writable": false,
        "description": "PV1 Parameter"
    },
    "13": {
        "name": "Wechselrichter-Modell",
        "type": "string",
        "writable": false,
        "description": "Wechselrichter-Modell"
    },
    "14": {
        "name": "Wechselrichter Seriennummer",
        "type": "string",
        "writable": false,
        "description": "Wechselrichter Seriennummer"
    },
    "15": {
        "name": "IMEI/IMSI",
        "type": "string",
        "writable": false,
        "description": "IMEI/IMSI"
    },
    "16": {
        "name": "Aktuelle Temperatur",
        "type": "value",
        "writable": false,
        "description": "Aktuelle Temperatur",
        "unit": "℃"
    },
    "28": {
        "name": "Leistungsdaten",
        "type": "raw",
        "writable": true,
        "description": "Leistungsdaten"
    },
    "29": {
        "name": "Betriebsstatus",
        "type": "raw",
        "writable": true,
        "description": "Betriebsstatus"
    },
    "101": {
        "name": "PV-Eingangsleistung",
        "type": "value",
        "writable": false,
        "description": "PV-Eingangsleistung",
        "unit": "W"
    },
    "102": {
        "name": "CO2-Einsparung",
        "type": "value",
        "writable": false,
        "description": "CO2-Einsparung",
        "unit": "Kg"
    },
    "103": {
        "name": "PV-Spannung",
        "type": "value",
        "writable": false,
        "description": "PV-Spannung",
        "unit": "V"
    },
    "104": {
        "name": "Inverter-Temperatur",
        "type": "value",
        "writable": false,
        "description": "Inverter-Temperatur",
        "unit": "℃"
    },
    "105": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": true,
        "description": "Zähler zurücksetzen"
    },
    "106": {
        "name": "AC-Strom",
        "type": "value",
        "writable": false,
        "description": "AC-Strom",
        "unit": "A"
    },
    "107": {
        "name": "Tagesverbrauch",
        "type": "value",
        "writable": false,
        "description": "Tagesverbrauch",
        "unit": "kW·h"
    },
    "108": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": true,
        "description": "Wechselrichter EIN/AUS"
    },
    "109": {
        "name": "AC-Ausgangsleistung",
        "type": "value",
        "writable": false,
        "description": "AC-Ausgangsleistung",
        "unit": "W"
    },
    "110": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": true,
        "description": "Leistungsbegrenzung",
        "unit": "%"
    },
    "111": {
        "name": "PV-Strom",
        "type": "value",
        "writable": false,
        "description": "PV-Strom",
        "unit": "A"
    },
    "112": {
        "name": "Virtuell gepflanzte Bäume",
        "type": "value",
        "writable": false,
        "description": "Virtuell gepflanzte Bäume",
        "unit": "pcs"
    },
    "113": {
        "name": "Gesamtenergieerzeugung",
        "type": "value",
        "writable": false,
        "description": "Gesamtenergieerzeugung",
        "unit": "kW·h"
    },
    "114": {
        "name": "AC-Spannung",
        "type": "value",
        "writable": false,
        "description": "AC-Spannung",
        "unit": "V"
    },
    "115": {
        "name": "Steckdosen Online-Status",
        "type": "string",
        "writable": false,
        "description": "Steckdosen Online-Status"
    },
    "116": {
        "name": "Steckdosenleistung",
        "type": "string",
        "writable": false,
        "description": "Steckdosenleistung"
    },
    "117": {
        "name": "Steckdosenverbrauch",
        "type": "raw",
        "writable": false,
        "description": "Steckdosenverbrauch"
    },
    "118": {
        "name": "Energiequelle",
        "type": "enum",
        "writable": false,
        "description": "Energiequelle",
        "options": [
            "0",
            "1",
            "2"
        ]
    },
    "119": {
        "name": "Anti-Feed-In-Schalter",
        "type": "bool",
        "writable": true,
        "description": "Anti-Feed-In-Schalter"
    },
    "120": {
        "name": "Batterie-Kapazität",
        "type": "value",
        "writable": false,
        "description": "Batterie-Kapazität",
        "unit": "%"
    },
    "121": {
        "name": "Gesamtleistung der Steckdosen",
        "type": "value",
        "writable": false,
        "description": "Gesamtleistung der Steckdosen",
        "unit": "W"
    },
    "122": {
        "name": "Knoten hinzufügen",
        "type": "bool",
        "writable": true,
        "description": "Knoten hinzufügen"
    },
    "123": {
        "name": "PV lädt Batterie",
        "type": "enum",
        "writable": false,
        "description": "PV lädt Batterie",
        "options": [
            "0",
            "1"
        ]
    },
    "124": {
        "name": "Gepaarte Knoten",
        "type": "string",
        "writable": false,
        "description": "Gepaarte Knoten"
    },
    "125": {
        "name": "Alle Knoten löschen",
        "type": "bool",
        "writable": true,
        "description": "Alle Knoten löschen"
    },
    "126": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": true,
        "description": "Arbeitsmodus",
        "options": [
            "0",
            "1"
        ]
    },
    "127": {
        "name": "Nennleistung (W)",
        "type": "value",
        "writable": false,
        "description": "Nennleistung (W)",
        "unit": "W"
    },
    "128": {
        "name": "Schnellberichtsmodus",
        "type": "bool",
        "writable": true,
        "description": "Schnellberichtsmodus"
    },
    "146": {
        "name": "INV-Modus setzen",
        "type": "value",
        "writable": true,
        "description": "INV-Modus setzen",
        "unit": ""
    }
}
