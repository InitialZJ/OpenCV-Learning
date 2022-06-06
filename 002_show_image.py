import cv2

img = cv2.imread('lena.jpg', 0)  # 灰度化读取
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()