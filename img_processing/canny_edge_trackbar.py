import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('../assets/browntrout.jpg',0)
canny = cv2.imread('../assets/browntrout.jpg',0)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('minVal','image',0,1000,nothing)
cv2.createTrackbar('maxVal','image',0,1000,nothing)
cv2.createTrackbar('aperture','image',0,5,nothing)
while(1):
    cv2.imshow('image',canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
 
# get current positions of four trackbars
    minV = cv2.getTrackbarPos('minVal','image')
    maxV = cv2.getTrackbarPos('maxVal','image')
    apert = cv2.getTrackbarPos('aperture','image')
    canny = cv2.Canny(img,minV,maxV,apert)  

cv2.destroyAllWindows()
