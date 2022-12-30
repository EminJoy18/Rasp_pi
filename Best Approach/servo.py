import RPi.GPIO as GPIO
import time
import pigpio
import os  
os.system ("sudo pigpiod")
import pada_navigation as pd
import circle_detection as cd

pwm1 = None
pwm2 = None
servo1 =13
servo2 = 19
reached_min_height = False
angles = [30,150,60,120,90,90,120,60,150,30,30,150,60,120,90,90,120,60,150,30,30,150,60,120,90,90,120,60,150,30,30,150,60,120,90,90,120,60,150,30]
"""
def pins_initializaton():
    global pwm1,pwm2

    pwm1 = pigpio.pi() 
    pwm1.set_mode(servo1, pigpio.OUTPUT)
    pwm1.set_PWM_frequency( servo1, 50 )
    
    pwm2 = pigpio.pi() 
    pwm2.set_mode(servo1, pigpio.OUTPUT)
    pwm2.set_PWM_frequency( servo2, 50 )
    
"""

def pins_initializaton():
    global pwm1,pwm2
    pwm1 = pigpio.pi()
    pwm1.set_mode(servo1, pigpio.OUTPUT)
    pwm1.set_PWM_frequency( servo1, 50 )
        
    pwm2 = pigpio.pi()
    pwm2.set_mode(servo2, pigpio.OUTPUT)
    pwm2.set_PWM_frequency( servo2, 50 )
"""
def pins_initializaton():
    global pwm1,pwm2
    gpio.setmode(gpio.BOARD)
    gpio.setup(35,gpio.OUT)
    gpio.setup(33, gpio.OUT)
    pwm1=gpio.PWM(35, 50)
    pwm2 = gpio.PWM(33,50)
    pwm1.start(0)
    pwm2.start(0)
def move_servo(deg1,deg2):
    global pwm1,pwm2
    pwm1.ChangeDutyCycle(giveMeDc(deg1))
    pwm2.ChangeDutyCycle(giveMeDc(deg2))
    time.sleep(0.5)
def giveMeDc(deg):
    dc = (deg//18)+2
    print(dc)
    return dc
"""
def getMePulse(deg):
    pw = round(11.11 * deg) + 500
    return pw

def control_servo():
    global pwm1,pwm2
    count = 0
    while (not pd.reached_min_height):
        pwm1.set_servo_pulsewidth( servo1,getMePulse(cd.move_servo_x)) ;
        pwm2.set_servo_pulsewidth( servo2,getMePulse(cd.move_servo_y)) ;
        #pwm1.set_servo_pulsewidth( servo1,getMePulse(deg1)) ;
        #pwm2.set_servo_pulsewidth( servo2,getMePulse(deg2)) ;
        pwm1.set_PWM_dutycycle(servo1, 0)
        pwm2.set_PWM_dutycycle(servo2, 0)
        pwm1.set_PWM_frequency( servo1, 0 )
        pwm2.set_PWM_frequency( servo2, 0 )

    """
    while :
        
        grid_x = cd.move_servo_x
        grid_y =cd.move_servo_x
        
        grid_x = angles[count]
        grid_y = angles[count+1]
        move_servo(grid_x,grid_y)
        time.sleep(1)
        count+=2
    pwm1.stop()
    pwm2.stop()
    gpio.cleanup()
    """
#pins_initializaton()
#time.sleep(3)
"""

while True:
    deg1,deg2 = map(int,input('Enter : ').split())
    control_servo(deg1,deg2)
    time.sleep(3)
"""
#pins_initializaton()
#control_servo(90,90)

