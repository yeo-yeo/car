Code to interact with the Arduino car. The flow is currently:

- Use MacOS Bluetooth Manager to pair to device (DSD TECH HC-05 or sometimes just says Bluetooth Device). This can be a pain and sometimes you seem to need to forget the device entirely, turn bluetooth off and on again, and pair afresh. Pin is 1234.
- Start server by just running node-server/index.mjs
- Run move_receiver.py. This is a script which opens a connection to the server, over which moves will be sent, and it will relay to the car over bluetooth.
- Start client by running npm run serve (in client dir)
- Visit localhost:3000 and click buttons. Car should move!


Or to talk to the prod server
- ./python/move_receiver.py prod
- https://car.rcdis.co