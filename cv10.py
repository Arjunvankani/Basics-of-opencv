import cv2

path = r'a.jpg'

image = cv2.imread(path)

window_name = 'Image'

image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)
  
cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()