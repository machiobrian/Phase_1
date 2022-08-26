import cv2 as cv
count = 0
#stop sign cascade classifier

# stop_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Signs/cascade_stop_sign.xml')
# left_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_Cascades/data_output/cascade.xml')
# right_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_right/data_output/cascade.xml')

stop_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/stop_cascade.xml')
left_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/left_cascade.xml')
right_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/right_cascade.xml')
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
    right_sign_scaled = right_sign.detectMultiScale(gray, 1.3,5)
    left_sign_scaled = left_sign.detectMultiScale(gray, 1.3,5)

    # Detect the stop sign, x,y = origin points, w = width, h = height
    for (x, y, w, h) in right_sign_scaled :
        # count += 1
        # print(count)
        stop_width = w
        stop_height = h
        print(stop_width, stop_height)

        #Draw rectangle around the stop sign
        stop_sign_rectangle = cv.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        #Write "Stop sign" on the bottom of the rectangle
        stop_sign_text = cv.putText(img=stop_sign_rectangle,
                                     text="Sign",
                                     org=(x, y+h+30),
                                     fontFace=cv.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv.LINE_4)
    cv.imshow("img", img)
    key = cv.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break