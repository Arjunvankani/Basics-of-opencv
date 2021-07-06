import numpy as np
import cv2

img = cv2.imread('cat_damaged.png')

mask = cv2.imread('cat_mask.png', 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imwrite('cat_inpainted.png', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()