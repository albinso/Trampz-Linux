from const import *
from convert import *
class Sensor():

	def __init__(self, details, peripheral):
		self.peripheral = peripheral
		self.details = details
		self.data = self.getCharacteristic(details["read"])
		self.config = self.getCharacteristic(details["config"])
		#self.period = self.getCharacteristic(details["period"])
		self.name = details["name"]

	def getCharacteristic(self, UUID):
		return self.peripheral.getCharacteristics(uuid=self.toTI(UUID))[0]

	def convert(self, data):
		if self.details == ACCELEROMETER:
			return convertAccelerometer(data)
		if self.details == HUMIDITY:
			return convertHumidity(data)
		if self.details == MAGNETOMETER:
			return convertMagnetometer(data)
		if self.details == BAROMETER:
			c = self.getCharacteristic(self.details["calibration"]).read()
			return convertBarometer(data, c)
		if self.details == GYROSCOPE:
			return convertGyroscope(data)
		return False

	def read(self):
		return self.convert(self.data.read())

	def configure(self, data):
		self.config.write(data)

	def enable(self, signal=ENABLE_SENSOR):
		self.configure(signal)

	def disable(self, signal=DISABLE_SENSOR):
		self.configure(signal)

	def toTI(self, UUID):
		return "F000" + UUID + "-0451-4000-B000-000000000000"

	def __str__(self):
		return self.name




