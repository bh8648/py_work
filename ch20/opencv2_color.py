# opencv2_color.py

import cv2

img = cv2.imread("./ch20/sample.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# cv2.imshow("Loaded Image", img)
cv2.imshow("Gray Image", gray)
# cv2.imshow("RGB Image", rgb)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





