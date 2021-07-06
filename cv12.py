import cv2
import numpy as np

FILE_NAME = 'a.jpg'
try:
	img = cv2.imread(FILE_NAME)

	(height, width) = img.shape[:2]

	res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

	cv2.imwrite('result12.jpg', res)


except IOError:
	print ('Error while reading files !!!')
