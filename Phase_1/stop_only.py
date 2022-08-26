"""
what i want to achieve:
    1. detect road sign - read function
    2. measure the distance btn stop sign and bot - distance function
    3. if dist > a_value_x, acknowlegde stop sign
    4. stop the bot - stop function
"""

#camera lib setup
import cv2 as cv

#camera function - read sign

def stop_camera():
    stop_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/left_cascade1.xml')
    cap = cv.VideoCapture(0) 
    while cap.isOpened():
        _, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

        #detect sign and draw rectangle round it
        for (x,y,w,h) in stop_sign_scaled:
            global stop_w
            stop_w = w
            global stop_h
            stop_h = h
            #print(stop_w, stop_h)
            measure_dist()

        cv.imshow("img", img)
        key = cv.waitKey(30)
        if key == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            break

#distance function
def measure_dist():
    """Since we have w and h, use it to determine dist from sign
    distance = far, close, stop"""
    #print(stop_w) #ccall this function inside a function
    pixel = 200
    max_pixel = 600
    if stop_w in range(pixel, max_pixel) and stop_h in range(pixel, max_pixel):
        print("stop bot")
    else:
        print("safe")
    

stop_camera()
measure_dist()