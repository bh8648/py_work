# opencv5_blur.py

import cv2

img = cv2.imread("./ch20/sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, ksize=(15,15), sigmaX=0)

# src: 입력 이미지

# ksize: 가우시안 커널 크기
# -> 커널 크기가 클수록 이미지가 더 부드러워 짐
# (0,0)을 지정하면 sigma 값에 의해 자동 결정됨 / 홀수로 지정해야 함 why? 홀수 크기 커널이어야 중앙 픽셀이 존재하며 대칭적 처리 가능
# 픽셀 주변 값 평균/가중평균 등으로 처리

# sigmaX : x방향 sigma
# sigmaY : y방향 sigma
# X와 Y 방향의 가우시안 표준편차(sigmaX, sigmaY).
# 0으로 설정하면 OpenCV가 자동으로 값을 계산





cv2.imshow("Gaussian Blur Image", blurred)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





