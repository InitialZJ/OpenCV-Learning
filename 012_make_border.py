import cv2
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]

img1 = cv2.imread('lena.jpg')

replicate = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLUE)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
replicate = cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB)
reflect = cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB)
reflect101 = cv2.cvtColor(reflect101, cv2.COLOR_BGR2RGB)
wrap = cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB)
constant = cv2.cvtColor(constant, cv2.COLOR_BGR2RGB)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
