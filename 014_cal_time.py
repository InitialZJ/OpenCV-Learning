import time
import cv2

img1 = cv2.imread('lena.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)  # 0.6414025

# img1 = cv2.imread('lena.jpg')
#
# e1 = time.time()
# for i in range(5, 49, 2):
#     img1 = cv2.medianBlur(img1, i)
#
# e2 = time.time()
# t = e2 - e1
# print(t)  # 0.662588357925415