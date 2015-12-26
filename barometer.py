from UUIDs import *
import binascii
import struct
import time
import sys, os
import struct
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))

from bluepy.bluepy.btle import UUID, Peripheral
 
def getMagnetism(data):
	x = data[2:4] + data[0:2]
	y = data[6:8] + data[4:6]
	z = data[10:12] + data[8:10]
	x = int(x, 16)
	y = int(y, 16)
	z = int(z, 16)

	return x, y, z

uuid = MAGNETOMETER["read"]
conf = MAGNETOMETER["config"]
temp_uuid = UUID("F000" + uuid + "-0451-4000-B000-000000000000")
conf_uuid = UUID("F000" + conf + "-0451-4000-B000-000000000000")
 
p = Peripheral("78:A5:04:19:58:E1")
conf = p.getCharacteristics(uuid=conf_uuid)[0]
sensorOn  = struct.pack("B", 0x01)
conf.write(sensorOn, withResponse=True)
try:
	ch = p.getCharacteristics(uuid=temp_uuid)[0]
	if (ch.supportsRead()):
		while 1:
			data = ch.read()
			val = binascii.b2a_hex(data)
			
			x, y, z = getMagnetism(val)
			print("X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))
 
finally:
	p.disconnect()