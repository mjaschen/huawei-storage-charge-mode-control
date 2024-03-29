"""Enable/disable storage charge from AC for Huawei LUNA2000 batteries."""

import argparse
import asyncio
import ipaddress
import sys
import traceback
from huawei_solar import HuaweiSolarBridge, HuaweiSolarException


def valid_ip(ip):
    """Ensure that the argument is a valid IPv4 address."""
    try:
        ipaddress.IPv4Address(ip)
        return ip
    except ValueError as validate_exception:
        raise argparse.ArgumentTypeError(f'{ip} is not a valid IPv4 address') \
            from validate_exception


def valid_port(port):
    """Ensure that the argument is a valid port number."""
    port = int(port)
    if port < 1 or port > 65535:
        raise argparse.ArgumentTypeError(f"{port} is not a valid port number (1-65535)")
    return port


def valid_inverter(inverter_id):
    """Ensure that the argument is a valid Modbus ID."""
    inverter_id = int(inverter_id)
    if inverter_id < 0 or inverter_id > 65535:
        raise argparse.ArgumentTypeError(f"{inverter_id} is not a valid Modbus slave ID (0-65535)")
    return inverter_id


def parse_arguments():
    """Setup command line arguments."""
    parser = argparse.ArgumentParser(
        description='Enable/disable storage charge from AC, show status'
    )
    parser.add_argument(
        'state',
        type=str,
        choices=['on', 'off', 'status'],
        help='State to set (on=allow charging from AC/off='
             'disallow charging from AC/status=show current state)'
    )
    parser.add_argument(
        '--ip',
        type=valid_ip,
        help='IP address of the Huawei Solar Dongle'
    )
    parser.add_argument(
        '--port',
        type=valid_port,
        default=502,
        help='Modbus TCP port number (default: 502)'
    )
    parser.add_argument(
        '--inverter',
        type=valid_inverter,
        help='Slave ID of the Inverter which controls the battery'
    )

    args = parser.parse_args()

    if args.ip is None:
        print("Error: No IP address provided.")
        sys.exit(1)

    if args.inverter is None:
        print("Error: No inverter ID provided.")
        sys.exit(1)

    return args


async def main(args):
    """Set the Modbus register to enable/disable storage charge from AC."""
    bridge = await HuaweiSolarBridge.create(
        args.ip,
        args.port,
        args.inverter
    )

    if args.state == 'status':
        registers = await bridge.update_configuration_registers()
        if registers['storage_charge_from_grid_function'].value:
            print("Storage charge from AC is currently enabled")
        else:
            print("Storage charge from AC is currently disabled")

        return

    value = 1 if args.state == 'on' else 0

    await bridge.set("storage_charge_from_grid_function", value)

if __name__ == "__main__":
    parsed_arguments = parse_arguments()
    try:
        asyncio.run(main(parsed_arguments))
    except HuaweiSolarException as exception:
        print("Error: cannot change the storage charge mode")
        traceback.print_exc()
        sys.exit(1)
