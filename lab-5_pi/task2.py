import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

# with picamera.PiCamera() as camera:
#     camera.resolution=(320,240)
#     time.sleep(3)
#     camera.capture('assets/pi_photo')
#     image = cv2.imread('assets/pi_photo')

window_name = '“lab 5.2'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,channels=image.shape #Add this line here

for x in range (0,height):
	for y in range (0,width):
		r,g,b=rgb[x,y]
		if r>g and r>b and r>128:
			image[x,y]=0,0,255


window_name2 = 'lab 5.2 red filter'
cv2.imshow(window_name2, image)
raw_key = cv2.waitKey(20000)
