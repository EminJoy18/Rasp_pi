import cv2
import numpy as np
#import sensor as se
from picamera.array import PiRGBArray
from picamera import PiCamera
print("Initializing Camera")
camera = PiCamera()
camera.resolution = (640, 480)
camera.zoom=(0.25,0.3333333333333,0.5,0.3333333333333)
rawCapture = PiRGBArray(camera, size=(640, 480))
colour_ranges = {"RED": [[170, 85, 110], [180, 255, 255], [0, 85, 110], [7, 255, 255]],
                 "BLUE": [[94, 80, 2], [126, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "PURPLE": [[129, 80, 10], [150, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "YELLOW": [[15, 40, 50], [40, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "ORANGE": [[10, 100, 20], [25, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "GREEN" : [[49, 30, 45], [85, 255, 255], [0, 0, 0], [0, 0, 0]]}

color = colour_ranges['GREEN']
low_coul_1 = np.array(color[0])
high_coul_1 = np.array(color[1])
low_coul_2 = np.array(color[2])
high_coul_2 = np.array(color[3])
    #while True:
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    key = cv2.waitKey(1)
    frame = frame.array
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 320))

    HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    coul_mask_1 = cv2.inRange(HSV_frame, low_coul_1, high_coul_1)
    coul_mask_2 = cv2.inRange(HSV_frame, low_coul_2, high_coul_2)

    full_coul_mask = coul_mask_2 + coul_mask_1
    kernel = np.ones((3, 3), np.uint8)
    full_coul_mask = cv2.erode(full_coul_mask, kernel)
    full_coul_mask = cv2.dilate(full_coul_mask, kernel)
    full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
    frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
    circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=150, param2=20, minRadius=0, maxRadius=30)
    
    #kernel = np.ones((3, 3), np.uint8)
    #full_coul_mask = cv2.erode(full_coul_mask, kernel)
    #full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
    #frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
    #circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=2, maxRadius=200)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
        diameter = (circles[0,2]) * 2
        #altitude = se.read_bmp388() * 3.28084
        print('[Circle Detected Successfully ]. . .')
        print('Diameter : ',circles[0, 2])
        #print('Altitude : ',altitude,' Diameter : ',diameter)
        #cv2.destroyAllWindows()
        
    
    
    cv2.imshow("Frame", frame)
    rawCapture.truncate(0)
    if key == 27:
        break
