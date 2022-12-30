# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library. so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC= 13 #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 700  #change this if your ESC's min value is different or leave it be
print ("For first time launch, select calibrate")
print ("Type the exact word for the function you want")
print ("calibrate OR manual OR control OR arm OR stop")

def manual_drive(): #You will use this function to program your ESC if required
    print ("You have successfully entered manual mode ")
    print ("now you've got multiple option enter stop , control (to make it work as per the set of predefined commands), arm and anything else to give custom input ")
    while True:
        inp = input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break   
        else:
            pi.set_servo_pulsewidth(ESC,inp)
                
def calibrate():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will hear two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print ("Weird eh! Special tone")
            time.sleep(7)
            print("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control() # You can change this to any other function you want
            
def control(): 
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
    print ("Controls -  down to decrease speed & up  to increase speed OR low to decrease a lot of speed & high to increase a lot of speed")
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = input()
        if (inp == "2"):
            speed -= 100    # decrementing the speed like hell
            print ("speed = %d" % speed)
        elif (inp == "1"):
            speed += 100    # incrementing the speed like hell
            print ("speed = %d" % speed)
        elif (inp == "0"):
            speed = 700    # incrementing the speed 
            print ("speed = %d" % speed)
        elif (inp == "3"):
            speed = 1900     # decrementing the speed
            print ("speed = %d" % speed)
        elif (inp == "w"):
             speed += 10     
             print ("speed = %d" % speed)
        elif (inp == "s"):
             speed -= 10     
             print ("speed = %d" % speed)
        elif (inp == "a"):
             speed += 1    
             print ("speed = %d" % speed)
        elif (inp == "d"):
             speed -= 1    
             print ("speed = %d" % speed)
        elif (inp == "69"):
             givemethrust()
        elif (inp == "stop"):
            stop()          #going for the stop function
            break
        elif (inp == "manual"):
            manual_drive()
            break
        elif (inp == "arm"):
            arm()
            break   
        else:
            print ("WHAT DID I SAY!! Press high,low,up,down (high low commands can be used for manoeuvering in 100's and up down for 10's) ")
            
def arm(): #This is the arming procedure of an ESC 
    print ("Connect the battery and press Enter")
    inp = input()    
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        control() 
        
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.    
print("if you've just started ensure to calibrate your motor and then arm the motor only and only after that start your working process")
inp = input()
if inp == ("manual"):
    manual_drive()
elif inp == ("calibrate"):
    calibrate()
elif inp == ("arm"):
    arm()
elif inp == ("control"):
    control()
elif inp == ("stop"):
    stop()
else :
    print ("I must have made some mistakes master it surely isn't you its me but can you enter one of the few inputs that is actually a function again")


def give_me_thrust():
    time.sleep(1)
    #brr = 700
    #pi.set_servo_pulsewidth(ESC, brr)
    #while(True):
        #cmd = input()
        #if(cmd != "stop"):
    print("how much thrust do you want (in percentage)")
    inp = int(input())
    time.sleep(1)
    thrust = 700 + ((inp/100)*1300)
    print("thrust but in pwm", thrust)
    brr = thrust
    pi.set_servo_pulsewidth(ESC, brr)
    return
    #else:
    #stop()
            