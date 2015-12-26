import struct

ACCELEROMETER = {"read": "AA11", "config": "AA12", "period": "AA13", "name": "Accelerometer"}
HUMIDITY = {"read": "AA21", "config": "AA22", "period": "AA23", "name": "Humidity"}
MAGNETOMETER = {"read": "AA31", "config": "AA32", "period": "AA33", "name": "Magnetometer"}
BAROMETER = {"read": "AA41", "config": "AA42", "calibration": "AA43", "period": "AA44", "name": "Barometer"}
GYROSCOPE = {"read": "AA51", "config": "AA52", "period": "AA53", "name": "Gyroscope"}

ENABLE_SENSOR  = struct.pack("B", 0x01)
def enableGyroscope(X=False, Y=False, Z=False):
	res = (1 if X else 0) + (2 if Y else 0) + (4 if Z else 0)
	return struct.pack("B", res)

def toTI(UUID):
	return "F000" + UUID + "-0451-4000-B000-000000000000"