DPS_METADATA = {
    "1": {
        "name": "Gesamtverbrauch (kWh)",
        "type": "value",
        "writable": True,
        "description": "Gesamtverbrauch (kWh)",
        "unit": "kW·h"
    },
    "3": {
        "name": "PV1 Parameter",
        "type": "raw",
        "writable": False,
        "description": "PV1 Parameter"
    },
    "13": {
        "name": "Wechselrichter-Modell",
        "type": "string",
        "writable": False,
        "description": "Wechselrichter-Modell"
    },
    "14": {
        "name": "Wechselrichter Seriennummer",
        "type": "string",
        "writable": False,
        "description": "Wechselrichter Seriennummer"
    },
    "15": {
        "name": "IMEI/IMSI",
        "type": "string",
        "writable": False,
        "description": "IMEI/IMSI"
    },
    "16": {
        "name": "Aktuelle Temperatur",
        "type": "value",
        "writable": False,
        "description": "Aktuelle Temperatur",
        "unit": "℃"
    },
    "28": {
        "name": "Leistungsdaten",
        "type": "raw",
        "writable": True,
        "description": "Leistungsdaten"
    },
    "29": {
        "name": "Betriebsstatus",
        "type": "raw",
        "writable": True,
        "description": "Betriebsstatus"
    },
    "101": {
        "name": "PV-Eingangsleistung",
        "type": "value",
        "writable": False,
        "description": "PV-Eingangsleistung",
        "unit": "W"
    },
    "102": {
        "name": "CO2-Einsparung",
        "type": "value",
        "writable": False,
        "description": "CO2-Einsparung",
        "unit": "Kg"
    },
    "103": {
        "name": "PV-Spannung",
        "type": "value",
        "writable": False,
        "description": "PV-Spannung",
        "unit": "V"
    },
    "104": {
        "name": "Inverter-Temperatur",
        "type": "value",
        "writable": False,
        "description": "Inverter-Temperatur",
        "unit": "℃"
    },
    "105": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": True,
        "description": "Zähler zurücksetzen"
    },
    "106": {
        "name": "AC-Strom",
        "type": "value",
        "writable": False,
        "description": "AC-Strom",
        "unit": "A"
    },
    "107": {
        "name": "Tagesverbrauch",
        "type": "value",
        "writable": False,
        "description": "Tagesverbrauch",
        "unit": "kW·h"
    },
    "108": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": True,
        "description": "Wechselrichter EIN/AUS"
    },
    "109": {
        "name": "AC-Ausgangsleistung",
        "type": "value",
        "writable": False,
        "description": "AC-Ausgangsleistung",
        "unit": "W"
    },
    "110": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": True,
        "description": "Leistungsbegrenzung",
        "unit": "%"
    },
    "111": {
        "name": "PV-Strom",
        "type": "value",
        "writable": False,
        "description": "PV-Strom",
        "unit": "A"
    },
    "112": {
        "name": "Virtuell gepflanzte Bäume",
        "type": "value",
        "writable": False,
        "description": "Virtuell gepflanzte Bäume",
        "unit": "pcs"
    },
    "113": {
        "name": "Gesamtenergieerzeugung",
        "type": "value",
        "writable": False,
        "description": "Gesamtenergieerzeugung",
        "unit": "kW·h"
    },
    "114": {
        "name": "AC-Spannung",
        "type": "value",
        "writable": False,
        "description": "AC-Spannung",
        "unit": "V"
    },
    "115": {
        "name": "Steckdosen Online-Status",
        "type": "string",
        "writable": False,
        "description": "Steckdosen Online-Status"
    },
    "116": {
        "name": "Steckdosenleistung",
        "type": "string",
        "writable": False,
        "description": "Steckdosenleistung"
    },
    "117": {
        "name": "Steckdosenverbrauch",
        "type": "raw",
        "writable": False,
        "description": "Steckdosenverbrauch"
    },
    "118": {
        "name": "Energiequelle",
        "type": "enum",
        "writable": False,
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
        "writable": True,
        "description": "Anti-Feed-In-Schalter"
    },
    "120": {
        "name": "Batterie-Kapazität",
        "type": "value",
        "writable": False,
        "description": "Batterie-Kapazität",
        "unit": "%"
    },
    "121": {
        "name": "Gesamtleistung der Steckdosen",
        "type": "value",
        "writable": False,
        "description": "Gesamtleistung der Steckdosen",
        "unit": "W"
    },
    "122": {
        "name": "Knoten hinzufügen",
        "type": "bool",
        "writable": True,
        "description": "Knoten hinzufügen"
    },
    "123": {
        "name": "PV lädt Batterie",
        "type": "enum",
        "writable": False,
        "description": "PV lädt Batterie",
        "options": [
            "0",
            "1"
        ]
    },
    "124": {
        "name": "Gepaarte Knoten",
        "type": "string",
        "writable": False,
        "description": "Gepaarte Knoten"
    },
    "125": {
        "name": "Alle Knoten löschen",
        "type": "bool",
        "writable": True,
        "description": "Alle Knoten löschen"
    },
    "126": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": True,
        "description": "Arbeitsmodus",
        "options": [
            "0",
            "1"
        ]
    },
    "127": {
        "name": "Nennleistung (W)",
        "type": "value",
        "writable": False,
        "description": "Nennleistung (W)",
        "unit": "W"
    },
    "128": {
        "name": "Schnellberichtsmodus",
        "type": "bool",
        "writable": True,
        "description": "Schnellberichtsmodus"
    },
    "146": {
        "name": "INV-Modus setzen",
        "type": "value",
        "writable": True,
        "description": "INV-Modus setzen",
        "unit": ""
    }
}
