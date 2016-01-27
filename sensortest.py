import sys, os
import binascii
import struct
from TIDelegate import TIDelegate
from MouseDelegate import MouseDelegate
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle
from btle import Peripheral, UUID
from sensor import Sensor
from const import *

p = Peripheral("78:A5:04:19:58:E1")
s = Sensor(BAROMETER, p)
s.enable(signal=struct.pack("B", 0x02))
s.enable()
while True:
	print(s.read())