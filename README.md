# EntryList-Configurator
Easy configurator for your EntryList file.
Feel free to contribute.

## Requirements
python 3.12+

## Usage
Have a .ini file for your input, and a .ini file that you want to override.

## Current Features
- Checks cars in input file and depending on if it's a traffic car, adds AI and removes skin.

Example:

INPUT
[CAR_0]
MODEL=ks_nissan_gtr
SKIN=jet_black/ADAn
...
RESTRICTOR=0

OUTPUT
[CAR_0]
MODEL=ks_nissan_gtr
SKIN=jet_black/ADAn
...
RESTRICTOR=0
AI=none

INPUT
[CAR_0]
MODEL=traffic_aegis_airport_bus
...
RESTRICTOR=0

OUTPUT
[CAR_0]
MODEL=traffic_aegis_airport_bus
...
RESTRICTOR=0
AI=fixed
