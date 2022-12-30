import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


imu.readSensor()
imu.computeOrientation()
print('*****data packet start******')
print (" Accel x: {0} ;  Accel y : {1} ; Accel z : {2}".format(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]))
print()
print ("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]))
print()
print ("Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]))
print()
print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw))
print('Net Accel : ',imu.AccelVals[0]+imu.AccelVals[1]+imu.AccelVals[2])
print('******data packet end********')
rul=imu.MagVals[0]
pish=imu.MagVals[1]
yu=imu.MagVals[2]

#time.sleep(5)

while True:
    imu.readSensor()
    imu.computeOrientation()
    print('*****data packet start******')
    print (" Accel x: {0} ;  Accel y : {1} ; Accel z : {2}".format(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]))
    print()
    print ("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]))
    print()
    print ("Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]))
    print()
    print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw)) 
    #print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll-rul,imu.pitch-pish,imu.yaw-yu))
    print('Net Accel : ',imu.AccelVals[0]+imu.AccelVals[1]+imu.AccelVals[2])
    print('******data packet end********')
    
    time.sleep(1)
    
    
