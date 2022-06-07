import cv2
import numpy as np

# 定义平移矩阵
M = np.array([[1, 0, 100],
             [0, 1, 50]], dtype=np.float32)

img = cv2.imread('lena.jpg')
h, w = img.shape[:2]

# 平移
res = cv2.warpAffine(img, M, (w, h))

# ------------------------------------------------

img2 = cv2.imread('lena_long.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img2.shape

# 定义旋转矩阵
M2 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.6)

dst = cv2.warpAffine(img2, M2, (cols, rows))

# ------------------------------------------------

img3 = cv2.imread('drawing.jpg')
rows3, cols3, ch3 = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M3 = cv2.getAffineTransform(pts1, pts2)

res3 = cv2.warpAffine(img3, M3, (cols3, rows3))

# ------------------------------------------------

img4 = cv2.imread('sudokusmall.jpg')
rows4, cols4, ch4 = img4.shape

pts1_4 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2_4 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M4 = cv2.getPerspectiveTransform(pts1_4, pts2_4)

# 仿射变换
res4 = cv2.warpPerspective(img4, M4, (300, 300))


cv2.imshow('res', res)
cv2.imshow('dst', dst)
cv2.imshow('res3', res3)
cv2.imshow('res4', res4)
cv2.waitKey(0)
cv2.destroyAllWindows()
