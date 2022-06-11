import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('box.jpg', 0)

# --------------------------------
# 为什么梯度的数据类型要用 cv2.CV_64F ？
# 因为从黑色到白色的梯度是正的，而从白色到黑色的梯度是负的。
# 如果不用 CV_64F，而使用和原图一致的 CV_8U，会无法检测是白色到黑色的梯度
# --------------------------------

# 错误示范
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

# 正确操作
sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()
