#!/usr/bin/env python3

import ipaddress
import subprocess
import platform

def ping(host):
    """Return True if host responds to ping."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        output = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception:
        return False

def sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    alive = []

    print(f"\n=== Ping Sweep: {subnet} ===")

    for host in network.hosts():
        host_str = str(host)
        if ping(host_str):
            print(f"[+] {host_str} is alive")
            alive.append(host_str)
        else:
            print(f"[-] {host_str} is down")

    print("\n=== Summary ===")
    print(f"Total hosts: {network.num_addresses - 2}")
    print(f"Alive: {len(alive)}")
    print(f"Down: {(network.num_addresses - 2) - len(alive)}")

    return alive

if __name__ == "__main__":
    subnet = input("Enter subnet (CIDR): ")
    sweep(subnet)