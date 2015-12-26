import sys, os
import binascii
import struct
from TIDelegate import TIDelegate
from MouseDelegate import MouseDelegate
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle
from btle import Peripheral, UUID




acc_uuid = UUID("F000AA11-0451-4000-B000-000000000000")
conf_uuid = UUID("F000AA12-0451-4000-B000-000000000000")
sensorOn  = struct.pack("B", 0x01)

 
p = Peripheral("78:A5:04:19:58:E1")
conf = p.getCharacteristics(uuid=conf_uuid)[0]
acc = p.getCharacteristics(uuid=acc_uuid)[0]
p.setDelegate(MouseDelegate(None))
conf.write(sensorOn)
while True:
	if p.waitForNotifications(1.0):
		continue
	#print("Waiting for notification")
	#print(binascii.b2a_hex(acc.read()))
	
