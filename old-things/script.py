#!/usr/bin/env python3
import requests
from PyQt5 import QtBluetooth


class bluetooth:
    def __init__(self, parent=None):
        print("running init")
        self.connectToRobot()

    def connectToRobot(self):
        self.sock = QtBluetooth.QBluetoothSocket(
            QtBluetooth.QBluetoothServiceInfo.RfcommProtocol
        )

        self.sock.connected.connect(self.connectedToBluetooth)
        self.sock.readyRead.connect(self.receivedBluetoothMessage)
        self.sock.disconnected.connect(self.disconnectedFromBluetooth)
        self.sock.error.connect(self.socketError)
        self.sock.pairingConfirmationRequested.connect(self.pairing_confirmation)
        port = 1
        self.sock.connectToService(
            QtBluetooth.QBluetoothAddress("00:14:03:05:09:BF"), port
        )

    def socketError(self, error):
        print(f"🚨 {self.sock.errorString()}")

    def connectedToBluetooth(self):
        print("connected!")
        # while True:
        #     self.sock.write("F".encode())

    def sendMessage(self, msg: str):
        self.sock.write(msg.encode())

    def disconnectedFromBluetooth(self):
        print("Disconnected from bluetooth")

    def receivedBluetoothMessage(self):
        print("received")
        while self.sock.canReadLine():
            line = self.sock.readLine()
            print(str(line, "utf-8"))

    def pairing_confirmation(self):
        print("Pairing confirmation requested")


# this code to listen to web server which will push commmands
# then this code should speak to BT car
def listen_to_sse(bt: bluetooth):
    response = requests.get("http://127.0.0.1:3000/sse", stream=True)
    for line in response.iter_lines():
        if line:
            msg = line.decode("utf-8")
            print(msg)
            # validate blah blah
            # bt.sendMessage(msg[-1])


if __name__ == "__main__":
    bt = bluetooth()
    # listen_to_sse(bt)
