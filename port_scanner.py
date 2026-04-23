#!/usr/bin/env python3

"""
Simple Port Scanner
Author: Aakash Gurung

Description:
A Python-based TCP port scanner for lab and learning purposes.
It resolves a hostname/IP, scans a user-defined port range,
and reports open ports with clean output.

Use only on systems you own or are authorized to test.
"""

import socket
from datetime import datetime


def port_scan(target, start_port, end_port):
    try:
        # Resolve hostname to IP
        ip = socket.gethostbyname(target)

        print("\n" + "=" * 60)
        print(f"Target        : {target}")
        print(f"Resolved IP   : {ip}")
        print(f"Port Range    : {start_port} - {end_port}")
        print(f"Scan Started  : {datetime.now()}")
        print("=" * 60 + "\n")

        open_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

            sock.close()

        print("\n" + "=" * 60)
        print("Scan Completed")
        print(f"Total Open Ports Found: {len(open_ports)}")

        if open_ports:
            print("Open Ports:", ", ".join(map(str, open_ports)))
        else:
            print("No open ports found.")

        print("=" * 60)

    except socket.gaierror:
        print("Error: Hostname could not be resolved.")

    except socket.error:
        print("Error: Could not connect to the target.")

    except KeyboardInterrupt:
        print("\nScan stopped by user.")


def main():
    print("=== Python Port Scanner ===")
    print("For authorized lab use only.\n")

    target = input("Enter target IP or hostname: ").strip()

    try:
        start_port = int(input("Enter start port (example: 1): "))
        end_port = int(input("Enter end port (example: 1024): "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range.")
            return

        port_scan(target, start_port, end_port)

    except ValueError:
        print("Please enter valid numeric port values.")


if __name__ == "__main__":
    main()
