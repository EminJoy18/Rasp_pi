import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(35,gpio.OUT)
gpio.setup(33, gpio.OUT)
pwm1=gpio.PWM(35, 50)
pwm2 = gpio.PWM(33,50)


def move_servo(deg1,deg2):
    pwm1.ChangeDutyCycle(giveMeDc(deg1))
    pwm2.ChangeDutyCycle(giveMeDc(deg2))
    time.sleep(0.5)

def giveMeDc(deg):
    dc = (deg//18)+2
    return dc

while True:
    ch = int(input('Enter : '))
    
    if(ch == 1):
        move_servo(0,180)
    elif(ch == 2):
        move_servo(180,0)
    elif(ch == 3):
        deg1,deg2 = map(int,input('Enter Angle : ').split())
        move_servo(deg1,deg2)
    elif(ch == 4 ):
        while(True):
            pwm1.start(0)
            pwm2.start(0)
            move_servo(60,60)
            pwm1.stop()
            pwm2.stop()
    else:
        move_servo(90,90)
        break
    

gpio.cleanup()

