import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lena.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2D直方图

# ---------------------------------------------
# OpenCV方法
# ---------------------------------------------
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# ---------------------------------------------
# numpy方法
# --------------------------------------------
h = hsv[:, 0]
s = hsv[:, 1]
v = hsv[:, 2]
hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

# 绘制2D直方图

# ---------------------------------------------
# OpenCV方法（不推荐）
# ---------------------------------------------
# cv2.imshow('hist', hist)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------------------------
# Matplotlib方法（推荐）
# ---------------------------------------------
plt.imshow(hist, interpolation='nearest')
plt.show()
