import time
import sensor as se

deg1 = 0
deg2 = 0
reached_min_height = False

def navigations(checkpoints,ground_val):
    global deg1, deg2, reached_min_height
    print('Lenght : ',len(checkpoints))
    while True:
        pada_altitude = abs(se.read_bmp388() - ground_val) 
        checkpoint_altitude = checkpoints[0]
        print('Altitude : ',pada_altitude)
        if pada_altitude > 0.5:
            dist = abs(pada_altitude - checkpoint_altitude)
            if pada_altitude > checkpoint_altitude:
                print(f'Move Down {dist} Meters')
                checkpoints.pop(0)
                """
                deg1 = 0
                deg2 = 0
                servo.move_servos(deg1,deg2)
                """
            elif pada_altitude < checkpoint_altitude:
                print('PADA is below the Checkpoint Altitude')
                if(dist <= 1):
                    print(f'Hold For Now {dist} Meters')
                else:
                    print(f'Move Up {dist} Meters')
                checkpoints.pop(0)
                """
                deg1 = 0
                deg2 = 0
                servo.move_servos(deg1,deg2)
                """
            elif pada_altitude == checkpoint_altitude:
                print('Good go to Next Checkpoint')
                checkpoints.pop(0)
        else:
            reached_min_height = True
            print('Propulsion Stop')
            break
        
        if(len(checkpoints) == 0):
            print('Last Checkpoints Crossed')
            break # Only for Now Change Later
        
        time.sleep(1)
    return           