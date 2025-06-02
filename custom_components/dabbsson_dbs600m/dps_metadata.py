DPS_METADATA = {
    "pv_power": {
        "name": "PV-Eingangsleistung",
        "type": "value",
        "writable": False,
        "description": "Photovoltaik-Eingangsleistung, Genauigkeit 0,01W",
        "unit": "W",
        "code": "pv_power",
        "dps": "101"
    },
    "emission": {
        "name": "CO2-Einsparung",
        "type": "value",
        "writable": False,
        "description": "Genauigkeit 0,01Kg",
        "unit": "Kg",
        "code": "emission",
        "dps": "102"
    },
    "pv_volt": {
        "name": "PV-Spannung",
        "type": "value",
        "writable": False,
        "description": "Präzision 0,01 Volt",
        "unit": "V",
        "code": "pv_volt",
        "dps": "103"
    },
    "temperature": {
        "name": "Inverter-Temperatur",
        "type": "value",
        "writable": False,
        "description": "Genauigkeit: 0,1℃",
        "unit": "℃",
        "code": "temperature",
        "dps": "104"
    },
    "clear_energy": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": True,
        "description": "Setzt die Energiezähler auf Null zurück",
        "code": "clear_energy",
        "dps": "105"
    },
    "ac_current": {
        "name": "AC-Strom",
        "type": "value",
        "writable": False,
        "description": "AC-Ausgangsstrom (Genauigkeit: 0.01 A)",
        "unit": "A",
        "code": "ac_current",
        "dps": "106"
    },
    "day_energy": {
        "name": "Tagesverbrauch",
        "type": "value",
        "writable": False,
        "description": "Tägliche erzeugte Energie (Genauigkeit 0.01 kWh)",
        "unit": "kW·h",
        "code": "day_energy",
        "dps": "107"
    },
    "switch": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": True,
        "description": "Schaltet den Wechselrichter ein oder aus",
        "code": "switch",
        "dps": "108"
    },
    "out_power": {
        "name": "AC-Ausgangsleistung",
        "type": "value",
        "writable": False,
        "description": "AC-Ausgangsleistung, Genauigkeit 0.01W",
        "unit": "W",
        "code": "out_power",
        "dps": "109"
    },
    "power_adjustment": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": True,
        "description": "Prozentuale Begrenzung der Ausgangsleistung",
        "unit": "%",
        "code": "power_adjustment",
        "dps": "110"
    },
    "pv_current": {
        "name": "PV-Strom",
        "type": "value",
        "writable": False,
        "description": "Strom vom PV-Modul (Genauigkeit 0.01 A)",
        "unit": "A",
        "code": "pv_current",
        "dps": "111"
    },
    "plant": {
        "name": "Virtuell gepflanzte Bäume",
        "type": "value",
        "writable": False,
        "description": "Kumulierter Baumbestand",
        "unit": "pcs",
        "code": "plant",
        "dps": "112"
    },
    "energy": {
        "name": "Gesamtenergieerzeugung",
        "type": "value",
        "writable": False,
        "description": "Gesamt erzeugte Energie (Genauigkeit 0.01 kWh)",
        "unit": "kW·h",
        "code": "energy",
        "dps": "113"
    },
    "ac_volt": {
        "name": "AC-Spannung",
        "type": "value",
        "writable": False,
        "description": "AC-Ausgangsspannung",
        "unit": "V",
        "code": "ac_volt",
        "dps": "114"
    },
    "power_src": {
        "name": "Energiequelle",
        "type": "enum",
        "writable": False,
        "description": "0: unbekannt, 1: PV, 2: Batterie",
        "options": ["0", "1", "2"],
        "code": "power_src",
        "dps": "118"
    },
    "anti_reflux_flag": {
        "name": "Anti-Feed-In-Schalter",
        "type": "bool",
        "writable": True,
        "description": "Aktiviert oder deaktiviert die Einspeisevermeidung",
        "code": "anti_reflux_flag",
        "dps": "119"
    },
    "bat_capacity": {
        "name": "Batterie-Kapazität",
        "type": "value",
        "writable": False,
        "description": "Ladezustand der Batterie in Prozent",
        "unit": "%",
        "code": "bat_capacity",
        "dps": "120"
    },
    "total_power": {
        "name": "Gesamtleistung der Steckdosen",
        "type": "value",
        "writable": False,
        "description": "Summierte Leistung aller Steckdosen",
        "unit": "W",
        "code": "total_power",
        "dps": "121"
    },
    "pv_to_bat": {
        "name": "PV lädt Batterie",
        "type": "enum",
        "writable": False,
        "description": "Ob PV aktuell die Batterie lädt (0/1)",
        "options": ["0", "1"],
        "code": "pv_to_bat",
        "dps": "123"
    },
    "node_paired": {
        "name": "Gepaarte Knoten",
        "type": "string",
        "writable": False,
        "description": "Informationen zu gepaarten Knoten",
        "code": "node_paired",
        "dps": "124"
    },
    "workmode": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": True,
        "description": "0: Energiesparmodus, 1: Batterielademodus",
        "options": ["0", "1"],
        "code": "workmode",
        "dps": "126"
    },
    "rated_power": {
        "name": "Nennleistung (W)",
        "type": "value",
        "writable": False,
        "description": "Nennleistung des Mikro-Wechselrichters",
        "unit": "W",
        "code": "rated_power",
        "dps": "127"
    },
    "up_flag": {
        "name": "Schnellberichtsmodus",
        "type": "bool",
        "writable": True,
        "description": "Aktiviert die sofortige Berichterstattung von Statusänderungen",
        "code": "up_flag",
        "dps": "128"
    },
    "add_node": {
        "name": "Knoten hinzufügen",
        "type": "bool",
        "writable": False,
        "description": "Ermöglicht das Hinzufügen eines Knotens",
        "code": "add_node",
        "dps": "129"
    },
    "delete_all_nodes": {
        "name": "Alle Knoten löschen",
        "type": "bool",
        "writable": False,
        "description": "Löscht alle gekoppelten Knoten",
        "code": "delete_all_nodes",
        "dps": "132"
    },
    "inv_mode_set": {
        "name": "INV-Modus setzen",
        "type": "value",
        "writable": True,
        "description": "Einstellung für INV-Betriebsmodus",
        "unit": "",
        "code": "inv_mode_set",
        "dps": "146"
    }
}
