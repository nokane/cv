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

