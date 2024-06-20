#!/usr/bin/env python3

import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("00:14:03:05:09:BF", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        client.send("F".encode())
        # (send message)
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    pass

client.close()
