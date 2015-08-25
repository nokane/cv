import cv2
import numpy as np
from matplotlib import pyplot as plt


# 2D convolution

img = cv2.imread('../assets/rabbit.png')
kernel = np.ones((5,5),np.float32)/25
print kernel
dst = cv2.filter2D(img,-1,kernel)

# Image Blurring/Smoothing
blur = cv2.blur(img,(5,5))

# Gaussian Blur

gaussBlur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(1,4,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1,4,2),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(1,4,3),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(1,4,4),plt.imshow(gaussBlur),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()

noisyImg = cv2.imread('../assets/noisy_image.png')
median = cv2.medianBlur(noisyImg,5)
bilateralBlur = cv2.bilateralFilter(noisyImg,9,75,75)

plt.subplot(1,3,1),plt.imshow(noisyImg),plt.title('Noisy Image')
plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(median),plt.title('Noisy Image after Median Blurring')
plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(bilateralBlur),plt.title('Noisy Image after Bilateral Blurring')
plt.xticks([]), plt.yticks([])
plt.show()
