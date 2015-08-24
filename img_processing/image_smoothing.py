import cv2
import numpy as np
from matplotlib import pyplot as plt


# 2D convolution

img = cv2.imread('../assets/rabbit.png')
kernel = np.ones((5,5),np.float32)/25
print kernel
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img, 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
