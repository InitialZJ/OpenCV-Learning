import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('wiki.jpg', cv2.IMREAD_GRAYSCALE)

# flatten() 将数组变成1维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# plt.plot(cdf_normalized, color='b')
# plt.hist(img.flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.legend(('cdf', 'histogram'), loc='upper left')
# plt.show()

# -------------------------------------------------------
# numpy方法
# -------------------------------------------------------
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img]

# flatten() 将数组变成1维
hist2, bins2 = np.histogram(img2.flatten(), 256, [0, 256])
# 计算累积分布图
cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2 * hist2.max() / cdf2.max()

# plt.subplot(221), plt.imshow(img, cmap='gray')
# plt.subplot(222), plt.plot(cdf_normalized, color='b'), plt.hist(img.flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.legend(('cdf', 'histogram'), loc='upper left')
#
# plt.subplot(223), plt.imshow(img2, cmap='gray')
# plt.subplot(224), plt.plot(cdf_normalized2, color='b'), plt.hist(img2.flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.legend(('cdf2', 'histogram2'), loc='upper left')
#
# plt.show()

# -------------------------------------------------------
# OpenCV方法
# -------------------------------------------------------
# img = cv2.imread('wiki.jpg', cv2.IMREAD_GRAYSCALE)
# equ = cv2.equalizeHist(img)
# res = np.hstack((img, equ))
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -------------------------------------------------------
# CLAHE有限对比适应性直方图均衡化
# -------------------------------------------------------
img = cv2.imread('tsukuba_l.jpg', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
res = np.hstack((img, cl1))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
