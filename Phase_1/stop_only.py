import cv2 as cv

stop_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/stop_cascade.xml')
left_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/left_1L.xml')
right_sign = cv.CascadeClassifier('/home/machio_b/Desktop/Final Semester/Project/Vision AGV/Phase_/Cascade_files/right_1R.xml')

#initialize a camera variable
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, gray = cap.read() #read frames in video
    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert to gray scale for processing

    stop_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
    right_scaled = right_sign.detectMultiScale(gray, 1.3, 5)
    left_scaled = left_sign.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in stop_scaled:
        rect = cv.rectangle(gray, (x,y),(x+w, y+h),(0, 255, 0), 3)
        print('stop')
    for (x,y,w,h) in right_scaled:
        rect = cv.rectangle(gray, (x,y),(x+w, y+h),(0, 255, 0), 3)
        print('right')
    for (x,y,w,h) in left_scaled:
        rect = cv.rectangle(gray, (x,y),(x+w, y+h),(0, 255, 0), 3)
        print('left')
    
    
    cv.imshow("Image", gray)
    key = cv.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break




