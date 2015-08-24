import cv2
import numpy as np
from matplotlib import pyplot as plt

# resize image
img = cv2.imread('../assets/browntrout.jpg')
height, width = img.shape[:2]
res = cv2.resize(img, (int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_CUBIC)
cv2.imshow('img',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

# shift the image's location

img = cv2.imread('../assets/browntrout.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,150]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#rotate the image 90 degrees counter clockwise

img = cv2.imread('../assets/browntrout.jpg', 0)
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

imgSudoku = cv2.imread('../assets/sudoku_img.jpg')
rows,cols,ch = imgSudoku.shape

pts1 = np.float32([[70,70],[70,140],[140,70],[140,140]])
pts2 = np.float32([[0,0],[0,250],[250,0],[250,250]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(imgSudoku,M,(250,250))

plt.subplot(121),plt.imshow(imgSudoku),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
