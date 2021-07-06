import cv2

path = r'a.jpg'

src = cv2.imread(path)

window_name = 'Image'

image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )

cv2.imshow(window_name, image)
cv2.waitKey(0)

cv2.destroyAllWindows()