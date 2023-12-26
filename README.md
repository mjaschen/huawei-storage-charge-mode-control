# Huawei Battery Charge Mode Control

This script allows you to control the battery charge mode of Huawei LUNA2000 batteries. It allows you to set the battery charge mode to "Allow Storage Charge From Grid" or "Do Not Allow Storage Charge From Grid".

## Requirements

- Python 3.9+

## Installation

- Clone this repository
- Create a virtual environment with `python -m venv venv`
- Install the requirements with `pip install -r requirements.txt`
- Copy the `.env.example` file to `.env` and fill in the required information (IP address for SDongle and Modbus ID for the inverter which the battery is connected to)

## Usage

```shell
# enable storage charge from grid
./enable.sh
# disable storage charge from grid
./disable.sh
# use the script directly
python ac-charge.py --ip 10.0.1.2 --inverter 16 on
# online help
python ac-charge.py -h
```
