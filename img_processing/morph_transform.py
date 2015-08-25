# Morphological Transformation

import cv2
import numpy as np

# Erosion
img = cv2.imread('../assets/j.png', 0)
kernel = np.ones((5,5),np.uint8)
print kernel
erosion = cv2.erode(img, kernel, iterations = 1)
cv2.imshow('img',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

#dilation
dilation = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow('img', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Opening - erosion followed by dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('img', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Closing - dilation followed by erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('img', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
