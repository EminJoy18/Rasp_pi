import circle_detection as cd
import time
import math
ckpts = []

isDistanceCalculated = False
distance_calculation_details = []
#speed = [12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,13,11,13]
run_speed = 1


def distance_calulation():
    global isDistanceCalculated,distance_calulation_details

    #count = 0
    timee = 0
    avg_speed = 0
    total_speed = 0
    while(not cd.isCircleDetacted_pa):
        print('Started . . .')
        #print('Speed : ',run_speed)
        time.sleep(1)
        timee += 1
        #total_speed += speed[count]
        total_speed += run_speed
        avg_speed = total_speed / timee
        #count += 1
        """
        if count == len(speed):
            print('Avg Speed :',avg_speed)
            break
        """
    avg_speed = round(avg_speed)        
    distance = avg_speed * timee
    print(f'Distance is {distance}')
    isDistanceCalculated = True
    distance_calculation_details = [avg_speed , timee , distance]
    print(distance_calculation_details)
    return distance_calculation_details

def giveMeCheckpoints(altittude,distance,speed):

    # drp_h = int(input("enter the hieght at which the plane was dropped: "))
    drp_h = altittude
    # calc_x = int(input("enter the calculated horizontal distance"))
    calc_x = distance
    slp = drp_h/calc_x
    incln = math.atan(slp)
    incln = incln*(180/math.pi)
    # a_speed = int(input("Enter the speed at which the pada is dropped"))
    a_speed = speed
    as_y = -1*(a_speed*math.sin(a_speed))
    as_x = a_speed*math.cos(a_speed)
    c_alt = drp_h
    c_dst = calc_x
    t = 1
    while(True):
        ckpts.append(round(c_alt))
        if ((t * as_y)<0):
            c_alt = drp_h + (t * as_y)
        else:
            c_alt = drp_h - (t * as_y)
        if(c_alt<5):
            break
        t = t+1
    
    return ckpts
