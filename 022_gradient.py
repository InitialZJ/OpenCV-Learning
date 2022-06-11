import cv2
import matplotlib.pyplot as plt

img = cv2.imread('dave.jpg', 0)

# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1，与原图保持一致np.uint8
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 参数 1, 0 只在 x 方向求一阶导数，最大可求 2 阶导数
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# 参数 0, 1 只在 y 方向求一阶导数，最大可求 2 阶导数
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('sobelx'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('sobely'), plt.xticks([]), plt.yticks([])
plt.show()
