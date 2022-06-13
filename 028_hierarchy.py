import cv2

img = cv2.imread('hierarchy.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# RETR_LIST 所有轮廓，不创建任何轮廓间的父子关系
contours, hierarchies = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchies)

# RETR_EXTERNAL 最外层的轮廓
contours, hierarchies = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchies)

# RETR_CCOMP 轮廓分成两组，外围轮廓一组，内含空洞轮廓一组
contours, hierarchies = cv2.findContours(img_gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchies)

# RETR_TREE 所有轮廓，并创建完整组织关系
contours, hierarchies = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchies)



# img = cv2.drawContours(img, contours, -1, (255, 0, 255), 3)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
