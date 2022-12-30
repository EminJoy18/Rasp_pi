import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.start_recording('my_video.h264')
    #time.sleep(2)
    for x in range(0,50):
        camera.zoom=(0.25,0.3333333333333,0.5,0.3333333333333)
        time.sleep(0.1)