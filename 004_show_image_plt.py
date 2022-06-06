import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)  # 灰度化读取
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
