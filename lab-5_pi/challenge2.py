from tkinter import X
import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io


def make_circle(img,center,radius,colour):
    for x in range (center[0]-radius,center[0]+radius):
        for y in range (center[1]-radius,center[1]+radius):
            print(x,y)
            x_vector = x - center[0]
            y_vector = y - center[1]
            if ((x_vector * x_vector) + (y_vector * y_vector)) <= radius * radius:
                img[x,y]=colour
    return img
    

# stream=io.BytesIO()
# with picamera.PiCamera() as camera:
# 	camera.resolution=(320,240)
# 	camera.framerate=24
# 	time.sleep(1)
# 	camera.capture(stream,format='jpeg')
# data=np.fromstring(stream.getvalue(),dtype=np.uint8)
# image=cv2.imdecode(data,1)

# with picamera.PiCamera() as camera:
# 	camera.resolution=(320,240)
# 	camera.capture('assets/pi_photo')
# image = cv2.imread('assets/pi_photo')

# image =cv2.imread('assets/0_Screen-Shot-2020-08-21-at-163535.png')
# image = cv2.resize(image, (320,240))

with picamera.PiCamera() as camera:
    camera.resolution=(320,240)
    time.sleep(3)
    camera.capture('assets/pi_photo')
    image = cv2.imread('assets/pi_photo')

image = make_circle(image,(100,24),4,[0,0,0])

cv2.imshow('window_name2', image)
raw_key = cv2.waitKey(20000)