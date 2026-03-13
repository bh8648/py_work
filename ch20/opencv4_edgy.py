# opencv4_edgy.py

# edge -> 색이 급격하게 변하는 지점

import cv2

img = cv2.imread("./ch20/sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# img: 입력이미지. 보통 그레이스케일 이미지를 사용

# threshold1: 엣지 검출에 사용되는 최소 임계값
# -> 너무 낮게 설정하면 원치않은 edge까지 검출

# threshold2: 엣지 검출에 사용되는 최대 임계값
# -> 너무 높게 설정하면 edge가 잘 검출되지 않음







cv2.imshow("Canny Edge Image", edges)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





