import numpy
import PIL
import math
import time
# import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

# stream=io.BytesIO()
# with picamera.PiCamera() as camera:
# 	camera.resolution=(320,240)
# 	camera.framerate=24
# 	time.sleep(1)
# 	camera.capture(stream,format='jpeg')
# data=np.fromstring(stream.getvalue(),dtype=np.uint8)
# image=cv2.imdecode(data,1)

image =cv2.imread('assets/0_Screen-Shot-2020-08-21-at-163535.png')
image = cv2.resize(image, (320,240))

image[120,64]=0,128,255

cv2.imshow('window_name2', image)
raw_key = cv2.waitKey(20000)

