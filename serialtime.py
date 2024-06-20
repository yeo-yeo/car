#!/usr/bin/env python3

import requests
import serial
import time


def main():
    connection = serial.Serial("/dev/tty.DSDTECHHC-05", 9600, timeout=1)

    try:
        response = requests.get("http://127.0.0.1:3000/sse", stream=True)
        for line in response.iter_lines():
            print(f"got http msg: {line}")
            if line:
                msg = line.decode("utf-8")
                print(msg)
                connection.write((msg + "\r\n").encode())
                # time.sleep(0.5)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        connection.close()  # Close the serial connection


if __name__ == "__main__":
    main()
