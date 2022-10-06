from email.mime import image
from tkinter import Frame
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

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))
	
	rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	for x in range (0,height):
		for y in range (0,width):
			r,g,b=rgb[x,y]
			if r>g and r>b and r>200:
				frame[x,y]=0,0,255

	cv2.imshow('window_name2', frame)
	if cv2.waitKey(1) == ord('q'):
			break

cap.release()
cv2.destroyAllWindows() #destroys all windows that cv2 has open