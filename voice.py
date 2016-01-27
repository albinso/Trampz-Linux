import dbus
import sys, os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle
from TIDelegate import TIDelegate
from pykeyboard import PyKeyboard
import pyttsx
import random
k = PyKeyboard()

def printText():
	print("")
engine = pyttsx.init()
voices = engine.getProperty('voices')


class SpotifyDelegate(TIDelegate):

	def __init__(self, params):
		TIDelegate.__init__(self, params)
		session = dbus.SessionBus.get_session()
		#spotify = session.get_object(
			#"org.mpris.MediaPlayer2.spotify",
			#"/org/mpris/MediaPlayer2")
		self.leftdown = makePluttenHappy #spotify.PlayPause
		self.rightdown = plutt#spotify.Next
		#self.bothdown = spotify.Previous
		
def plutt():
	global voices
	i = random.randrange(len(voices))
	engine = pyttsx.init()
	engine.say("ess q")
	engine.runAndWait()
def makePluttenHappy():
	global voices
	#i = random.randrange(len(voices))
	engine = pyttsx.init()
	#engine.setProperty('voice', voices[i].id)
	engine.setProperty('volume', 1)
	engine.say("peeniss")
	engine.runAndWait()
	#k.type_string("penizs")


ADDRESS = "78:A5:04:19:58:E1"

conn = btle.Peripheral(ADDRESS)
conn.setDelegate(SpotifyDelegate(None))
print("Ready")
while True:
	if conn.waitForNotifications(1.0):
		continue
