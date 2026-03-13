# opencv1.py

import cv2

img = cv2.imread("./ch20/sample.jpg")
print(type(img))
print(img.shape)

dsize = (300,300) # 픽셀 단위로 리사이징
resized = cv2.resize(img, dsize)
print(resized.shape)



# cv2.imshow("Loaded Image", img)
cv2.imshow("Resized Image", resized)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





