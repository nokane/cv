import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('minVal','image',0,1000,nothing)
cv2.createTrackbar('maxVal','image',0,1000,nothing)
while(1):
    _, frame = cap.read()
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
 
    minV = cv2.getTrackbarPos('minVal','image')
    maxV = cv2.getTrackbarPos('maxVal','image')
    canny = cv2.Canny(frame,minV,maxV)  
    cv2.imshow('image',canny)

cv2.destroyAllWindows()
