import cv2

import numpy as np

path = r'a.jpg'

image = cv2.imread(path)

window_name = 'Image'

kernel = np.ones((6, 6), np.uint8)

cv2.imshow("Original", image)

image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()