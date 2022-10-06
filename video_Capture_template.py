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


cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))
	
	cv2.imshow('window_name2', frame)
	if cv2.waitKey(1) == ord('q'):
			break

cap.release()
cv2.destroyAllWindows() #destroys all windows that cv2 has open