import cv2
import numpy as numpy
img = cv2.imread('../assets/browntrout.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)