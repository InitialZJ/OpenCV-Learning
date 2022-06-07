import cv2

img = cv2.imread('lena.jpg')

# 缩用 INTER_AREA，放用 INTER_CUBIC

# 按比例缩
res1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 按大小放
h, w = img.shape[:2]
res2 = cv2.resize(img, (int(1.5 * w), int(1.5 * h)), interpolation=cv2.INTER_CUBIC)

cv2.imshow('res1', res1)
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
