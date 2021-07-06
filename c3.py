
import cv2
import os

image_path = r'a.jpg'

# Image directory
directory = r'dir_path'


img = cv2.imread(image_path)

os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = 'savedImage.jpg'

cv2.imwrite(filename, img)

print("After saving image:")
print(os.listdir(directory))
print('Successfully saved')
