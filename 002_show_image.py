import cv2

img = cv2.imread('lena.jpg', 0)  # 灰度化读取
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.namedWindow('img', cv2.WINDOW_NORMAL)  # 指定WINDOW_NORMAL窗口，可拉伸
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
