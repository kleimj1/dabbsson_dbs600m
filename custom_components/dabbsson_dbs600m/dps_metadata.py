DPS_METADATA = {
    "101": {
        "name": "PV-Eingangsleistung",
        "type": "value",
        "writable": False,
        "description": "PV-Leistung",
        "unit": "W",
        "code": "forward_energy_total"
    },
    "103": {
        "name": "PV-Spannung",
        "type": "value",
        "writable": False,
        "description": "PV-Spannung",
        "unit": "V",
        "code": "pv_volt"
    },
    "104": {
        "name": "Inverter-Temperatur",
        "type": "value",
        "writable": False,
        "description": "Temperatur",
        "unit": "℃",
        "code": "temperature"
    },
    "105": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": True,
        "description": "Zähler zurücksetzen",
        "code": "clear_energy"
    },
    "108": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": True,
        "description": "Schaltet den Wechselrichter",
        "code": "switch"
    },
    "109": {
        "name": "AC-Ausgangsleistung",
        "type": "value",
        "writable": False,
        "description": "AC-Leistung",
        "unit": "W",
        "code": "out_power"
    },
    "110": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": True,
        "description": "Limit in Prozent",
        "unit": "%",
        "code": "power_adjustment"
    },
    "111": {
        "name": "PV-Strom",
        "type": "value",
        "writable": False,
        "description": "PV-Strom",
        "unit": "A",
        "code": "pv_current"
    },
    "120": {
        "name": "Batterie-Kapazität",
        "type": "value",
        "writable": False,
        "description": "Batterie-SoC",
        "unit": "%",
        "code": "bat_capacity"
    },
    "126": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": True,
        "description": "Moduswahl",
        "options": ["0", "1"],
        "code": "workmode"
    }
}