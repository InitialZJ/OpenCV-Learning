import cv2

cap = cv2.VideoCapture(0)

# 获取摄像头默认分辨率 - 640 * 480
print(cap.get(3))
print(cap.get(4))

# 设置分辨率
cap.set(3, 320)
cap.set(4, 240)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is not True:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()