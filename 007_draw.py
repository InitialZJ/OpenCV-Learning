import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画直线，指定起点和终点坐标
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 画矩形，指定左上角和右下角坐标
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 画圆，指定中心点坐标和半径大小，-1代表充满封闭形状内部
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 画椭圆，指定中心点坐标，长轴和短轴长度，沿逆时针方向旋转的角度，沿顺时针方向起始的角度和结束角度
cv2.ellipse(img, (256, 256), (100, 50), 45, 0, 180, (0, 255, 0), -1)

# 画多边形，指定各个端坐标
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 0, 255), 3)

# 绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()