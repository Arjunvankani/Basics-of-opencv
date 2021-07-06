import cv2
import numpy as np

FILE_NAME = 'a.jpg'
try:
	img = cv2.imread(FILE_NAME)

	edges = cv2.Canny(img, 100, 200)
	
	cv2.imwrite('result15.jpg', edges)
except IOError:
	print ('Error while reading files !!!')
