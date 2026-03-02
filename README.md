# Zero Trust IoT Security – Simulation Code

This repository contains Python-based simulation code used to evaluate
authentication and security mechanisms for IoT networks.

## Implemented Methods
- Token-based authentication
- ECC-based authentication
- ECC + Zero Trust + IDS (Proposed)

## Experiments
The following experiments are implemented and used to generate results in the paper:
- Authentication Success Rate
- Replay Attack Detection Rate
- Latency Overhead
- Energy Consumption

## How to Run
Install dependencies:
```bash
pip install matplotlib



python results_authentication.py
python results_replay_attack.py
python results_latency.py
python results_energy.py
