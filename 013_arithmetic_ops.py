import cv2
import numpy as np

# 图像加法
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))  # 255，推荐
print(x + y)  # 4，不推荐

# 图像混合
# img1 = cv2.imread('lena.jpg')
# img2 = cv2.imread('lzj.jpg')
#
# dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 按位运算
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv_logo_white.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
