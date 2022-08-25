#motor module initialization
import sys, tty, termios
from gpiozero import Motor, PWMOutputDevice
from time import sleep

pwm_pin = 10 #initialize a single pwm pin to control all four pins

#motor pins 
m_f_l = [9,11]
m_f_r = [5,0]
m_r_r = [13,6]
m_r_l = [26,19]

motors = [
    Motor(m_f_l[1], m_f_l[0], pwm=False),
    Motor(m_f_r[0], m_f_r[1], pwm=False),
    Motor(m_r_l[0], m_r_l[1], pwm=False),
    Motor(m_r_r[0], m_r_r[1], pwm=False)
]
pwm_out = PWMOutputDevice(pwm_pin)

#camera module initialization
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time

#configuration
res = (320,240)
frame_rate = 15

#initialize the camera
camera = PiCamera()
camera.resolution = res
camera.framerate = frame_rate
camera.rotation = 0
rawCapture = PiRGBArray(camera, size=res)


#stop_sign module initialization
stop_sign = cv.CascadeClassifier('/home/pi/Phase_/Phase_1/cascade_stop_sign.xml')

#-------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------

def control_algo():
    # list to convert key into motor on/off values to correspond with direction
    # direction is based on keypad 

    current_dir = "stop"
    speed = 72
    pwm_out.value = (speed/100)

    while True:
        if (current_dir == "stop"):
            motors[0].backward()
            motors[1].backward()
            motors[2].backward()
            motors[3].backward()
            print('sign')
        else:
            motors[0].forward()
            motors[1].forward()
            motors[2].forward()
            motors[3].forward()
            print('sign_else')

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
                                      (0,255,0),1)


        #the corresponding actions for detection: here is where the motor control for stop
        #ought to be placed.
        # print("STOP")
        # count += 1
        # print(count)
        control_algo()

            
    #print(image.shape)
    cv.imshow("frame", image)
    key = cv.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord('q'):
        break

