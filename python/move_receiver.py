#!/usr/bin/env python3

import requests
import serial
import time
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: ./script_name.py <ENV>")
        sys.exit(1)
    
    if sys.argv[1] == 'prod':
        url = "https://car.rcdis.co/sse"
    else:
        url = "http://127.0.0.1:3000/sse"

    # The connection needs to have already been set up in Bluetooth manager (or somewhere)
    connection = serial.Serial("/dev/tty.DSDTECHHC-05", 9600, timeout=1)

    try:
        print("Opening HTTP SSE connection")
        response = requests.get(url, stream=True)
        print("Connection opened")
        for line in response.iter_lines():
            print(f"Got message: {line}")
            if line.decode("utf-8") == "data:connected":
                pass
            if line:
                # cut off the 'data:' prefix
                msg = line.decode("utf-8")[5:]
                connection.write((msg + "\r\n").encode())
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("Closing")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
