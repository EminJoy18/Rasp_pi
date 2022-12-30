from threading import Thread
import time 
import circle_detection as cd
#import sensor as se
#import somethingontheinternet as so
#import distance_measurement as dm
#import pada_navigation as pada_nav
import servo as sv

def start_process_of_PADA(details,col):
    print('In')
    ground_val = 41.185
    #print('Value Readed From Ground')
    #vertical_distance = se.read_bmp388() - ground_val
    #print('vd : ',vertical_distance)
    #checkpoints = dm.giveMeCheckpoints(se.read_bmp388()-27.8,details[2],10)
    #checkpoints = dm.giveMeCheckpoints(vertical_distance,details[2],0.5)
    #print('Checkpoints : ',checkpoints)
    
    pada_grid = Thread(target = cd.pada_colour_det , args=(col,))
    #pada_navi = Thread(target = pada_nav.navigations , args=(checkpoints,ground_val))
    pada_grid.start()
    time.sleep(3)
    print('[ Circle Detection Started ] . . .')
    #pada_navi.start()
    print('[ Navigation Started ] . . .')
    sv.pins_initializaton()
    sv.control_servo()
    return
    """
    """