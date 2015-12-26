import sys, os
import binascii
from TIDelegate import TIDelegate
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle
from pymouse import PyMouse

class MouseDelegate(TIDelegate):

	def __init__(self, params):
		TIDelegate.__init__(self, params)
		self.mouse = PyMouse()

	def handleAcceleration(self, data):
		x = data[0]*10 - 1
		y = data[1]*10
		z = data[2]*10
		print(data)
		pos = self.mouse.position()
		self.mouse.move(pos[0]+x, pos[1]+y)
		pass
