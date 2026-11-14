# Frappe Container Terminal Operating System (TOS) Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maritime](https://img.shields.io/badge/Maritime-TOS%20Port%20Operations-cyan.svg)](https://shipping.gov.in)

Maritime Port Terminal Operating System (TOS) for container yard block 3D slotting (Bay-Row-Tier), cold-chain reefer monitoring, and demurrage detention billing.

## Features
- **Yard 3D Slot Allocator:** Efficient spatial placement for 20ft and 40ft dry, hazardous, and refrigerated containers.
- **Reefer Plug Status:** Real-time electricity monitoring for cold-chain pharmaceuticals and food cargo.
- **Demurrage & Storage Surcharges:** Automatic gate-out hold release linked to dwell fees settlement.

## Tests
```bash
python3 -m unittest discover tests
```
