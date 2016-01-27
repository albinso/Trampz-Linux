from const import *
from convert import *
import binascii
import struct
import time
import sys, os
import struct
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
from bluepy.bluepy.btle import UUID, Peripheral


p = Peripheral("78:A5:04:19:58:E1")

for sensor in SENSORS:
	conf = p.getCharacteristics(uuid=toTI(sensor["config"]))[0]
	if sensor["name"] == "Gyroscope":
		conf.write(enableGyroscope(True, True, True))
	else:
		conf.write(ENABLE_SENSOR)


characteristics = [p.getCharacteristics(uuid=toTI(sensor["read"]))[0] for sensor in SENSORS]

while True:
	readings = list()
	for char in characteristics:
		data = char.read()
		readings.append(data)

	print("A: " + str(convertAccelerometer(readings[0])))
	print("H: " + str(convertHumidity(readings[1])))
	print("M: " + str(convertMagnetometer(readings[2])))
	print("B: " + str(convertBarometer(readings[3])))
	print("G: " + str(convertGyroscope(readings[4])))
	print("")
	time.sleep(5)