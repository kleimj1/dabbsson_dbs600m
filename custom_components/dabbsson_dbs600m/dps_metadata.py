DPS_METADATA = {
    "101": {
        "name": "PV-Eingangsleistung",
        "type": "value",
        "writable": false,
        "description": "Photovoltaik-Eingangsleistung, Genauigkeit 0,01W",
        "unit": "W",
        "code": "pv_power"
    },
    "102": {
        "name": "CO2-Einsparung",
        "type": "value",
        "writable": false,
        "description": "Genauigkeit 0,01Kg",
        "unit": "Kg",
        "code": "emission"
    },
    "103": {
        "name": "PV-Spannung",
        "type": "value",
        "writable": false,
        "description": "Präzision 0,01 Volt",
        "unit": "V",
        "code": "pv_volt"
    },
    "104": {
        "name": "Inverter-Temperatur",
        "type": "value",
        "writable": false,
        "description": "Genauigkeit: 0,1℃",
        "unit": "℃",
        "code": "temperature"
    },
    "105": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": true,
        "description": "Setzt die Energiezähler auf Null zurück",
        "code": "clear_energy"
    },
    "106": {
        "name": "AC-Strom",
        "type": "value",
        "writable": false,
        "description": "AC-Ausgangsstrom (Genauigkeit: 0.01 A)",
        "unit": "A",
        "code": "ac_current"
    },
    "107": {
        "name": "Tagesverbrauch",
        "type": "value",
        "writable": false,
        "description": "Tägliche erzeugte Energie (Genauigkeit 0.01 kWh)",
        "unit": "kW·h",
        "code": "day_energy"
    },
    "108": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": true,
        "description": "Schaltet den Wechselrichter ein oder aus",
        "code": "switch"
    },
    "109": {
        "name": "AC-Ausgangsleistung",
        "type": "value",
        "writable": false,
        "description": "AC-Ausgangsleistung, Genauigkeit 0.01W",
        "unit": "W",
        "code": "out_power"
    },
    "110": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": true,
        "description": "Prozentuale Begrenzung der Ausgangsleistung",
        "unit": "%",
        "code": "power_adjustment"
    },
    "111": {
        "name": "PV-Strom",
        "type": "value",
        "writable": false,
        "description": "Strom vom PV-Modul (Genauigkeit 0.01 A)",
        "unit": "A",
        "code": "pv_current"
    },
    "112": {
        "name": "Virtuell gepflanzte Bäume",
        "type": "value",
        "writable": false,
        "description": "Kumulierter Baumbestand",
        "unit": "pcs",
        "code": "plant"
    },
    "113": {
        "name": "Gesamtenergieerzeugung",
        "type": "value",
        "writable": false,
        "description": "Gesamt erzeugte Energie (Genauigkeit 0.01 kWh)",
        "unit": "kW·h",
        "code": "energy"
    },
    "114": {
        "name": "AC-Spannung",
        "type": "value",
        "writable": false,
        "description": "AC-Ausgangsspannung",
        "unit": "V",
        "code": "ac_volt"
    },
    "118": {
        "name": "Energiequelle",
        "type": "enum",
        "writable": false,
        "description": "0: unbekannt, 1: PV, 2: Batterie",
        "options": [
            "0",
            "1",
            "2"
        ],
        "code": "power_src"
    },
    "119": {
        "name": "Anti-Feed-In-Schalter",
        "type": "bool",
        "writable": true,
        "description": "Aktiviert oder deaktiviert die Einspeisevermeidung",
        "code": "anti_reflux_flag"
    },
    "120": {
        "name": "Batterie-Kapazität",
        "type": "value",
        "writable": false,
        "description": "Ladezustand der Batterie in Prozent",
        "unit": "%",
        "code": "bat_capacity"
    },
    "121": {
        "name": "Gesamtleistung der Steckdosen",
        "type": "value",
        "writable": false,
        "description": "Summierte Leistung aller Steckdosen",
        "unit": "W",
        "code": "total_power"
    },
    "123": {
        "name": "PV lädt Batterie",
        "type": "enum",
        "writable": false,
        "description": "Ob PV aktuell die Batterie lädt (0/1)",
        "options": [
            "0",
            "1"
        ],
        "code": "pv_to_bat"
    },
    "124": {
        "name": "Gepaarte Knoten",
        "type": "string",
        "writable": false,
        "description": "Informationen zu gepaarten Knoten",
        "code": "node_paired"
    },
    "126": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": true,
        "description": "0: Energiesparmodus, 1: Batterielademodus",
        "options": [
            "0",
            "1"
        ],
        "code": "workmode"
    },
    "127": {
        "name": "Nennleistung (W)",
        "type": "value",
        "writable": false,
        "description": "Nennleistung des Mikro-Wechselrichters",
        "unit": "W",
        "code": "rated_power"
    },
    "128": {
        "name": "Schnellberichtsmodus",
        "type": "bool",
        "writable": true,
        "description": "Aktiviert die sofortige Berichterstattung von Statusänderungen",
        "code": "up_flag"
    },
    "129": {
        "name": "Knoten hinzufügen",
        "type": "bool",
        "writable": false,
        "description": "Ermöglicht das Hinzufügen eines Knotens",
        "code": "add_node"
    },
    "132": {
        "name": "Alle Knoten löschen",
        "type": "bool",
        "writable": false,
        "description": "Löscht alle gekoppelten Knoten",
        "code": "delete_all_nodes"
    },
    "146": {
        "name": "INV-Modus setzen",
        "type": "value",
        "writable": true,
        "description": "Einstellung für INV-Betriebsmodus",
        "unit": "",
        "code": "inv_mode_set"
    }
}
