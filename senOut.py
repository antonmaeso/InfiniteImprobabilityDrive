import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

#i2c = busio.I2C(board.SCL, board.SDA)
#sensor1 = adafruit_fxos8700.FXOS8700(i2c)#accel and mag
#sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)#gyro

class sensor1(object):#mock sensor data
    accelerometer = [1,2,3]
    magnetometer = [1,2,3]

class sensor2(object):#mock sensor data
    gyroscope = [1,2,3]


def AccelX():
    return sensor1.accelerometer[0]

def AccelY():
    return sensor1.accelerometer[1]

def AccelZ():
    return sensor1.accelerometer[2]

def MagX():
    return sensor1.magnetometer[0]

def MagY():
    return sensor1.magnetometer[1]

def MagZ():
    return sensor1.magnetometer[2]

def GyroX():
    return sensor2.gyroscope[0]

def GyroY():
    return sensor2.gyroscope[1]

def GyrogZ():
    return sensor2.gyroscope[2]
