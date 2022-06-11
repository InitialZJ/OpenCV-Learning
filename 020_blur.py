import cv2

img = cv2.imread('opencv_logo.jpg')

# 平均
blur = cv2.blur(img, (5, 5))

# 高斯模糊
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# 中值模糊
median_blur = cv2.medianBlur(img, 5)

# 双边滤波
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Original', img)
cv2.imshow('Blurred', blur)
cv2.imshow('GaussianBlurred', gaussian_blur)
cv2.imshow('MedianBlurred', median_blur)
cv2.imshow('BilateralFiltered', bilateral_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
