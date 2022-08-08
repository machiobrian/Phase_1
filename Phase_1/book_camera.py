from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2 as cv
#set the params for capture size and image quality
size = (320, 240)
encode_param = [int(cv.IMWRITE_JPEG_QUALITY), 90]

#function to set up the camera
def setup_camera():
    camera = PiCamera()
    camera.resolution = size
    camera.rotation = 180
    return camera

#function to start capturing a stream of images - video, a frame at a time
def start_stream(camera):
    image_storage = PiRGBArray(camera, size=size)
    cam_stream = camera.capture_continuous(image_storage,
    format='bgr', use_video_port=True)

    #we are to loop through cam_stream until we choose to stop
    for raw_frame in cam_stream:
        yield raw_frame.array
        image_storage.truncate(0)

def get_encoded_bytes_for_frame(frame):
    result, encoded_image = cv.imencode('.jpg', frame, encode_param)
    return encoded_image.tostring()