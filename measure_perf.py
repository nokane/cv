# measuring performance with OpenCV
import cv2
import numpy as np

img1 = cv2.imread('assets/browntrout.jpg')
cv2.setUseOptimized(False)

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()

time = (e2 - e1)/ cv2.getTickFrequency()
print time

