import cv2
import numpy as np


# 腐蚀
img = cv2.imread('j.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

# 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)

# 开运算：先腐蚀，后膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算：先膨胀，后腐蚀
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 梯度：膨胀与腐蚀的差别
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

kernel2 = np.ones((13, 13), np.uint8)

# 礼帽：原图 - 开运算
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)

# 黑帽：闭运算 - 原图
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)

# kernel形状选择
print(cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
print(cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)))

cv2.imshow('img', img)
cv2.imshow('erode', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
