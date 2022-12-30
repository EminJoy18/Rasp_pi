import circle_detection as cd
import distance_measurement as dm
from threading import Thread
import time

def start_process_of_PA():
    color_detection = Thread(target = cd.pa_colour_det , args=('RED',))
    calculate_speed = Thread(target = dm.distance_calulation)
    color_detection.start()
    time.sleep(2)
    print('Bhaag Saaqib . . . ')
    calculate_speed.start()
    return

def find_distance():
    while(True):
        if(cd.isCircleDetacted and dm.isDistanceCalculated):
            det = dm.distance_calulation_details
            print('Avg Speed : ',det[0])
            print('Time Taken : ',det[1])
            print('Total Distance : ',det[2])
            break
    return det