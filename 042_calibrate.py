import cv2
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

objpoints = []
imgpoints = []

img = cv2.imread('left01.jpg')

# 寻找棋盘点
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

if ret:
    objpoints.append(objp)

    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)

# 标定相机
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 图像矫正
img = cv2.imread('left02.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# 方法1（推荐）：
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# 方法2：
# mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
# dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# 裁剪
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv2.imshow('dst', dst)
cv2.waitKey(0)

# 计算误差
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error

print(mean_error / len(objpoints))

cv2.destroyAllWindows()
