import cv2

higher_reso = cv2.imread('lena.jpg')

# 向上构建金字塔，尺寸变小，分辨率降低
lower_reso = cv2.pyrDown(higher_reso)

# 向下构建金字塔，尺寸变大，分辨率不变
higher_reso2 = cv2.pyrUp(lower_reso)
cv2.imshow('higher_reso', higher_reso)
cv2.imshow('lower_reso', lower_reso)
cv2.imshow('higher_reso2', higher_reso2)
cv2.waitKey(0)
cv2.destroyAllWindows()
