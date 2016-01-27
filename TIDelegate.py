import sys, os
import binascii
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle

class TIDelegate(btle.DefaultDelegate):
	def __init__(self, params):
		btle.DefaultDelegate.__init__(self)
		self.leftdown = do_nothing
		self.rightdown = do_nothing
		self.bothdown = do_nothing

		self.leftup = do_nothing
		self.rightup = do_nothing
		self.bothup = do_nothing
		self.state = 0
		# ... initialise here

	def calcAcceleration(self, val):
		v = (val * 1.0) / (64);
		return v
	

	def handleAcceleration(self, data):
		pass

	def handleNotification(self, cHandle, data):
		"""
		00 - No buttons are pressed
		01 - Right button is pressed
		02 - Left Button is pressed
		03 - Both buttons are pushed.
		Calls the appropriate function for the given indata.
		"""
		data = binascii.b2a_hex(data)

		if cHandle == 0x2D:
			data = self.readAccelerationData(data)
			
			self.handleAcceleration(data)
		if data == "00":
			if self.state == "02":
				self.leftup()
			if self.state == "01":
				self.rightup()
			if self.state == "03":
				self.bothup()
			self.state = "00"
			return

		if self.state != "00":
			return
			
		if data == "02":
			#print("Hey")
			self.leftdown()
		if data == "01":
			self.rightdown()
		if data == "03":
			self.bothdown()
		self.state = data

	

def do_nothing():
	pass