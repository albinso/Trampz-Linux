import binascii

"""
Contains functions for converting sensordata to useful formats.
"""
def hexToInt(hx, n_bytes=2):
	i = int(hx, 16)
	if n_bytes == 1:
		if i > 127:
			i -= 256
	if n_bytes == 2:
		if i > 256*256/2-1:
			i -= 256*256
	return i

def convertAccelerometer(data):
	data = binascii.b2a_hex(data)
	x = getByte(data, 0)
	y = getByte(data, 1)
	z = getByte(data, 2)
	x = hexToInt(x, n_bytes=1)
	y = hexToInt(y, n_bytes=1)
	z = hexToInt(z, n_bytes=1)
	return calcAcc(x), calcAcc(y), calcAcc(z)

def convertHumidity(data):
	data = binascii.b2a_hex(data)
	temp = getByte(data, 1) + getByte(data, 0)
	hum = getByte(data, 3) + getByte(data, 2)
	temp = hexToInt(temp)
	hum = hexToInt(hum)
	return calcHum(temp, hum)

def convertMagnetometer(data):
	data = binascii.b2a_hex(data)
	x = getByte(data, 1) + getByte(data, 0)
	y = getByte(data, 3) + getByte(data, 2)
	z = getByte(data, 5) + getByte(data, 4)
	x = hexToInt(x)
	y = hexToInt(y)
	z = hexToInt(z)

	return calcMagn(x), calcMagn(y), calcMagn(z)

def convertBarometer(data, cal):
	data = binascii.b2a_hex(data)
	cal = binascii.b2a_hex(cal)
	temp = getByte(data, 1) + getByte(data, 0)
	pres = getByte(data, 3) + getByte(data, 2)
	temp = hexToInt(temp)
	pres = hexToInt(pres)
	calibration = readCalibration(cal)
	return calcBar(temp, pres, calibration)

def convertGyroscope(data):
	data = binascii.b2a_hex(data)
	x = getByte(data, 1) + getByte(data, 0)
	y = getByte(data, 3) + getByte(data, 2)
	z = getByte(data, 5) + getByte(data, 4)
	x = hexToInt(x)
	y = hexToInt(y)
	z = hexToInt(z)

	return x, y, z

def getByte(data, i):
	return data[i*2:i*2+2]

def readCalibration(calibration):
	calibs = list()
	for i in range(0, 4):
		c = getByte(calibration, i+1) + getByte(calibration, i)
		c = int(c, 16)
		calibs.append(c)

	for i in range(4, 8):
		c = getByte(calibration, i+1) + getByte(calibration, i)
		c = hexToInt(c)
		calibs.append(c)
	return calibs

def calcAcc(raw):
	return (1.0*raw)/64

def calcHum(temp, hum):
	return -46.85 + 175.72/65536 * float(temp), -6.0 + 125.0/65536*float(hum)

def calcMagn(raw):
	return (raw * 1.0) / (65536.0/2000)

def calcBar(r_temp, pres, calibration):
	print(r_temp)
	print(pres)
	print(calibration)
	val = calibration[0]*r_temp*100
	print(val)
	temp = val >> 24
	val = calibration[1]*100
	temp += val >> 10

	sensitivity = calibration[2] + (calibration[3]*r_temp >> 17)
	sensitivity += (calibration[4]*r_temp**2) >> 34

	offset = calibration[5] * 2**14
	offset += (calibration[6]*r_temp) >> 3
	offset += (calibration[7]*r_temp**2) >> 19
	pres = (sensitivity * pres + offset) >> 14
	return temp, pres

