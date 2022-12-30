import os
import sys
import time
import smbus
from imusensor.MPU9250 import MPU9250
import board
import adafruit_bmp3xx
i2c = board.I2C()
#bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
#bmp.sea_level_pressure = 1011.176
"""
"""

def read_mpu():
	address = 0x68
	bus = smbus.SMBus(1)
	imu = MPU9250.MPU9250(bus, address)
	imu.begin()

	while True:
		imu.readSensor()
		imu.computeOrientation()
		print ("Accel x: {0} ; Accel y : {1} ; Accel z : {2}".format(round(imu.AccelVals[0],2),round(imu.AccelVals[1],2), round(imu.AccelVals[2],2)))
		print ("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(round(imu.GyroVals[0],2),round( imu.GyroVals[1],2), round(imu.GyroVals[2],2)))
		print ("Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(round(imu.MagVals[0],2),round(imu.MagVals[1],2), round(imu.MagVals[2],2)))
		print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(round(imu.roll,2),round(imu.pitch,2),round(imu.yaw,2)))
		time.sleep(0.1)
read_mpu()
"""

def read_bmp():
    altitude = round(bmp.altitude,2)
    print('Altitude : ',altitude)
    return altitude

read_bmp()
"""