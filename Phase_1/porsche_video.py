from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

#configuration
res = (320,240)
frame_rate = 15

stop_sign = cv.CascadeClassifier('/home/pi/Phase_/Phase_1/cascade_stop_sign.xml')

#initialize the camera
camera = PiCamera()
camera.resolution = res
camera.framerate = frame_rate
rawCapture = PiRGBArray(camera, size=res)

#allow the camera to do a push up
time.sleep(0.1)
count = 0

#capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format='bgr',
use_video_port=True):
    image = frame.array
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(image_gray, 1.3, 5)
    
    for (x,y,w,h) in stop_sign_scaled:
        #draw a rectangle around the stop sign
        stop_sign_rect = cv.rectangle(image, (x,y),
                                      (x+w,y+h),
                                      (0,255,256),3)
        print("STOP")
        
        count += 1
        print(count)

          
    #print(image.shape)
    cv.imshow("frame", image)
    key = cv.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord('q'):
        break
