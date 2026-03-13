# opencv3_rotation.py

import cv2

img = cv2.imread("./ch20/sample.jpg")
# h = img.shape[0]
# w = img.shape[1]
(h, w) = img.shape[:2]

center = (w//2, h//2) # 회전 중심 좌표. (x, y) 튜플

M = cv2.getRotationMatrix2D(center, angle=45, scale=1.0)
# angle = 회전각도. 음수는 시계 방향
# scale: 추가적인 확대 비율

rocated = cv2.warpAffine(img, M, (w+100, h+100))



# cv2.imshow("Loaded Image", img)
cv2.imshow("Rocated Image", rocated)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





