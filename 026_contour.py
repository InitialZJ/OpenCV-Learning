import cv2
import numpy as np

img = cv2.imread('j.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, 0)

# cv2.CHAIN_APPROX_SIMPLE 只会找出刚好能够包围的轮廓点，cv2.CHAIN_APPROX_NONE 所有的轮廓点都被找出，冗余
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# -1 代表所有轮廓都画
img = cv2.drawContours(img, contours, -1, (255, 0, 255), 3)

contour = contours[0]
# 矩
M = cv2.moments(contour)

# 轮廓面积
area = cv2.contourArea(contour)

# 轮廓周长，第二个参数指定轮廓是闭合的还是打开的
perimeter = cv2.arcLength(contour, True)

# 轮廓近似
epsilon = 0.1 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)

# 凸包
hull = cv2.convexHull(contour)

# 凸性检测
k = cv2.isContourConvex(contour)

# 直边界矩形
x, y, w, h = cv2.boundingRect(contour)
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# 旋转的边界矩形
rect = cv2.minAreaRect(contour)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 255, 255), 2)

# 最小外接圆
(x, y), radius = cv2.minEnclosingCircle(contour)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (255, 0, 255), 2)

# 椭圆拟合
ellipse = cv2.fitEllipse(contour)
img = cv2.ellipse(img, ellipse, (0, 255, 0), 2)

# 直线拟合
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)


cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
