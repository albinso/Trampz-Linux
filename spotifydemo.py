import dbus
import sys, os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle
from TIDelegate import TIDelegate



def printText():
	print("Hej")

class SpotifyDelegate(TIDelegate):

	def __init__(self, params):
		TIDelegate.__init__(self, params)
		session = dbus.SessionBus.get_session()
		spotify = session.get_object(
			"org.mpris.MediaPlayer2.spotify",
			"/org/mpris/MediaPlayer2")
		self.leftdown = spotify.Previous
		self.rightdown = spotify.Next
		self.bothdown = spotify.PlayPause


ADDRESS = "78:A5:04:19:58:E1"

conn = btle.Peripheral(ADDRESS)
conn.setDelegate(SpotifyDelegate(None))

while True:
	if conn.waitForNotifications(1.0):
		continue
