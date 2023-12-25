import argparse
import asyncio
import ipaddress
from huawei_solar import HuaweiSolarBridge
import sys

def valid_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return ip
    except ValueError:
        raise argparse.ArgumentTypeError(f"{ip} is not a valid IPv4 address")


def valid_port(port):
    port = int(port)
    if port < 1 or port > 65535:
        raise argparse.ArgumentTypeError(f"{port} is not a valid port number (1-65535)")
    return port


def valid_inverter(inverter_id):
    inverter_id = int(inverter_id)
    if inverter_id < 0 or inverter_id > 65535:
        raise argparse.ArgumentTypeError(f"{inverter_id} is not a valid Modbus slave ID (0-65535)")
    return inverter_id


def parse_arguments():
    parser = argparse.ArgumentParser(description='Enable/disable storage charge from AC.')
    parser.add_argument('state', type=str, choices=['on', 'off'], help='State to set (on=allow charging from AC/off=disallow charging from AC)')
    parser.add_argument('--ip', type=valid_ip, help='IP address of the Huawei Solar Dongle')
    parser.add_argument('--port', type=valid_port, default=502, help='Modbus TCP port number (default: 502)')
    parser.add_argument('--inverter', type=valid_inverter, help='Slave ID of the Inverter which controls the battery')

    args = parser.parse_args()

    if args.ip is None:
        print("Error: No IP address provided.")
        sys.exit(1)

    if args.inverter is None:
        print("Error: No inverter ID provided.")
        sys.exit(1)

    return args


async def main(args):
    value = 1 if args.state == 'on' else 0

    bridge = await HuaweiSolarBridge.create(
        args.ip,
        args.port,
        args.inverter
    )

    await bridge.set("storage_charge_from_grid_function", value)

if __name__ == "__main__":
    args = parse_arguments()
    try:
        asyncio.run(main(args))
    except:
        print("Error: cannot chnage the storage charge mode")
        sys.exit(1)
