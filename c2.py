
import cv2

path = r'a.jpg'

img = cv2.imread(path, 0)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
