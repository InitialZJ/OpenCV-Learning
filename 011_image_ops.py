import cv2

img = cv2.imread('lena.jpg')
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

print(img.shape)  # h, w, c

print(img.size)  # 像素数

print(img.dtype)  # 像素类型

# eye = img[247: 285, 242: 291]
# img[218: 256, 282: 331] = eye

b, g, r = cv2.split(img)
img = cv2.merge([b, g, r])

# 尽量用numpy索引，避免用split和merge
b = img[:, :, 0]

img[:, :, 2] = 0



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
