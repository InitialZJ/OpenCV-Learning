import cv2
import numpy as np

img = cv2.imread('blue.jpg')

# 转换到HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设定蓝色的阈值
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# 根据阈值构建掩膜
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 对原图像和掩膜进行位运算
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
