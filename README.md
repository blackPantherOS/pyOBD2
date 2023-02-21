pyOBD2
=====
Is a OBD-II compliant car diagnostic tool.
It is designed to interface with low-cost ELM 32x OBD-II diagnostic interfaces such as ELM-USB. It will basically allow you to talk to your car's ECU,... display fault codes, display measured values, read status tests, etc. All cars made since 1996 (in the US) or 2001 (in the EU) must be OBD-II compliant, i.e. they should work with pyOBD.
pyOBD is written entirely in Python and was originally written by Donour Sizemore, now maintained and improved by SECONS Ltd. and forked here.  It is Free Software and is distributed under the terms of the GPL.
(Old Python2 version http://www.obdtester.com/pyobd)

### General OBD-II information
Connect to a vehicle	Display tests status	View live sensor data	Read and clear fault codes
For Python devlopers, pyOBD provides a single module, obd_io, that allows high level control over sensor data and diagnostic trouble code managment.

### Requirements
An ELM 32x OBD-II interface
Python 3.x or greater (tested on python3.11)
python3-serial
wx with PyEvent (ex. wxpython4)
A car supporting OBD-II

### Quick Start on Linux
# under blackPanther OS

```bash
 usermod -a -G dialout [your_user_name]
 installing python3-wxpython4
 git clone https://github.com/blackPantherOS/pyOBD2
 cd pyOBD2
./pyobd2
```

# Debian based

```bash
sudo usermod -a -G dialout [your_user_name]
sudo apt-get install python3-wxpython4
git clone https://github.com/blackPantherOS/pyOBD2
cd pyOBD2
./pyobd2
```

### Hacking Guide
You can communicate directy with you ELM over screen.
```bash
screen /dev/ttyACM0 38400
```
Then use commands given from:
https://www.sparkfun.com/datasheets/Widgets/ELM327_AT_Commands.pdf

### Additions In This Fork
* Ability to query all realtime sensor messages and decode most given the formulas from: http://en.wikipedia.org/wiki/OBD-II_PIDs
* Remove sensors from list that are not supported by the connected auto.

### TODO
* Obtain a more complient ELM32x reader that can forward CAN messages: https://www.sparkfun.com/products/9555
* Add a CAN messages tab that will display raw messages
* Add decoding for known CAN messages
* Add hooks to the sensor tab for related CAN messages

