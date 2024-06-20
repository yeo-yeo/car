#!/usr/bin/env python3

# simple inquiry example
import bluetooth

# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print("Found {} devices.".format(len(nearby_devices)))

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name))

bd_addr = "00:14:03:05:09:BF"

port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
sock.send("F\r\n")
