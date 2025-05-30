DPS_METADATA = {
    "1": {
        "name": "Gesamtverbrauch (kWh)",
        "type": "value",
        "writable": False,
        "description": "Mapped to 'forward_energy_total'",
        "code": "forward_energy_total",
        "unit": "kW·h"
    },
    "105": {
        "name": "Zähler zurücksetzen",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'clear_energy'",
        "code": "clear_energy"
    },
    "108": {
        "name": "Wechselrichter EIN/AUS",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'switch'",
        "code": "switch"
    },
    "110": {
        "name": "Leistungsbegrenzung",
        "type": "value",
        "writable": True,
        "description": "Mapped to 'power_adjustment'",
        "code": "power_adjustment",
        "unit": "%"
    },
    "119": {
        "name": "Anti-Feed-In",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'anti_reflux_flag'",
        "code": "anti_reflux_flag"
    },
    "122": {
        "name": "Knoten hinzufügen",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'add_node'",
        "code": "add_node"
    },
    "125": {
        "name": "Alle Knoten löschen",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'delete_all_nodes'",
        "code": "delete_all_nodes"
    },
    "126": {
        "name": "Arbeitsmodus",
        "type": "enum",
        "writable": True,
        "description": "Mapped to 'workmode'",
        "code": "workmode",
        "options": ["0", "1"]
    },
    "128": {
        "name": "Schnellberichtsmodus",
        "type": "bool",
        "writable": True,
        "description": "Mapped to 'up_flag'",
        "code": "up_flag"
    },
    "146": {
        "name": "INV-Modus setzen",
        "type": "value",
        "writable": True,
        "description": "Mapped to 'inv_mode_set'",
        "code": "inv_mode_set",
        "unit": ""
    }
}