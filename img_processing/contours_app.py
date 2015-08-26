import numpy as np
import cv2

img = cv2.imread('../assets/greenbldg.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
_, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
