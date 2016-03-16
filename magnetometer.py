
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
