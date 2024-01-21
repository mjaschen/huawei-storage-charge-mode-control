# Huawei Battery Charge Mode Control

This script allows you to control the battery charge mode of Huawei LUNA2000 batteries. It allows you to set the battery charge mode to "Allow Storage Charge From Grid" or "Do Not Allow Storage Charge From Grid".

Also the current status of the battery charge mode setting can be queried.

## Requirements

- Python 3.10+

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
# show current status for the "charge from grid" setting
./status.sh
# use the script directly
python ac_charge.py --ip 10.0.1.2 --inverter 16 on
# online help
python ac_charge.py -h
```

## Return Values for Bridge

### Configuration Registers

```
{'storage_backup_power_state_of_charge': Result(value=0.0, unit='%'),
 'storage_capacity_control_mode': Result(value=<StorageCapacityControlMode.DISABLE: 0>, unit=None),
 'storage_capacity_control_periods': Result(value=[], unit=None),
 'storage_capacity_control_soc_peak_shaving': Result(value=50.0, unit='%'),
 'storage_charge_from_grid_function': Result(value=True, unit=None),
 'storage_charging_cutoff_capacity': Result(value=100.0, unit='%'),
 'storage_discharging_cutoff_capacity': Result(value=7.0, unit='%'),
 'storage_excess_pv_energy_use_in_tou': Result(value=<StorageExcessPvEnergyUseInTOU.FED_TO_GRID: 0>, unit=None),
 'storage_fixed_charging_and_discharging_periods': Result(value=[], unit=None),
 'storage_grid_charge_cutoff_state_of_charge': Result(value=50.0, unit='%'),
 'storage_maximum_charging_power': Result(value=2500, unit='W'),
 'storage_maximum_discharging_power': Result(value=2500, unit='W'),
 'storage_maximum_power_of_charge_from_grid': Result(value=3000, unit='W'),
 'storage_power_of_charge_from_grid': Result(value=3000, unit='W'),
 'storage_time_of_use_charging_and_discharging_periods': Result(value=[HUAWEI_LUNA2000_TimeOfUsePeriod(start_time=0, end_time=360, charge_flag=<ChargeFlag.CHARGE: 0>, days_effective=(True, True, True, True, True, True, True)), HUAWEI_LUNA2000_TimeOfUsePeriod(start_time=480, end_time=1320, charge_flag=<ChargeFlag.DISCHARGE: 1>, days_effective=(True, True, True, True, True, True, True))], unit=None),
 'storage_working_mode_settings': Result(value=<StorageWorkingModesC.MAXIMISE_SELF_CONSUMPTION: 2>, unit=None)}
```
