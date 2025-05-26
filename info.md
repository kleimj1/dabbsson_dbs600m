# Dabbsson DBS600M

This custom integration allows native support for the Dabbsson DBS600M in Home Assistant via local MQTT communication.

## Features

- Monitor PV power, voltage, and current
- Monitor inverter temperature and battery SoC
- Read AC output power
- Full local MQTT control, no cloud required

## Requirements

- Home Assistant 2023.5 or higher
- Working MQTT broker (e.g., Mosquitto)

## Setup

After installing via HACS:
1. Restart Home Assistant.
2. Add the integration via the Home Assistant UI.
3. Enter your Dabbsson's MQTT topic base and a name.
