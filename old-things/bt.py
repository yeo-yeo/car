#!/usr/bin/env python3

import sys
import os
import time
import threading


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtBluetooth


# this code works!! dont need to pair in the bluetooth manager first. (need to have connected at some point for PIN etc)
# why does this work and the other one doesn't.
# something to do with this super and widget whatnot
class bluetoothTest(QWidget):
    # class bluetoothTest(QWidget):

    def __init__(self, parent=None):
        super(bluetoothTest, self).__init__(parent)
        self.connectToRobot()
        self.win = QWidget()
        self.win.show()
        self.ready = False

    def connectToRobot(self):
        self.sock = QtBluetooth.QBluetoothSocket(
            QtBluetooth.QBluetoothServiceInfo.RfcommProtocol
        )

        self.sock.connected.connect(self.connectedToBluetooth)
        self.sock.readyRead.connect(self.receivedBluetoothMessage)
        self.sock.disconnected.connect(self.disconnectedFromBluetooth)
        self.sock.error.connect(self.socketError)
        port = 1
        self.sock.connectToService(
            QtBluetooth.QBluetoothAddress("00:14:03:05:09:BF"), port
        )

    def socketError(self, error):
        print(f"🚨 {self.sock.errorString()}")

    def connectedToBluetooth(self):
        self.ready = True
        print("connected!")
        print("write message (on connect)")
        write = self.sock.write("F\r\n".encode())
        # print(f"write result: {write}")
        # end = "\r\n"
        # writedata = self.sock.writeData(f"F{end * 400}".encode())
        # print(f"write data result: {writedata}")
        # one = self.sock.waitForBytesWritten(-1)
        # print(f"wait for b written result{one}")
        # time.sleep(3)
        # print("write message")
        # self.sock.write("R\r\n".encode())
        # # self.sock.waitForBytesWritten(-1)
        # time.sleep(3)
        # print("write message")
        # self.sock.write("F\r\n".encode())
        # self.sock.waitForBytesWritten(-1)

    def sendMessage(self, message):
        print("send message (from fn)")
        write = self.sock.write(f"{message}\r\n".encode())
        # print(f"write result: {write}")

    def disconnectedFromBluetooth(self):
        print("Disconnected from bluetooth")

    def receivedBluetoothMessage(self):
        print("received msg")
        while self.sock.canReadLine():
            line = self.sock.readLine()
            print(str(line, "utf-8"))


def main():
    app = QApplication(sys.argv)
    ex = bluetoothTest()

    # set up web listener thing

    variable = app.exec_() # this then blocks

    while not ex.ready:
        print('microsleep!')
        time.sleep(0.5)
        pass

    if ex.ready == True:
        print("ready!")
        time.sleep(3)
        ex.sendMessage("F")
        time.sleep(3)
        ex.sendMessage("F")
    else:
        print("wasnt ready")

    sys.exit(variable)


if __name__ == "__main__":
    main()
