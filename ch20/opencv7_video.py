# opencv7_video.py

import cv2

# 1. 이미지 파일 읽기


# vc = cv2.VideoCapture(0) # 웹캠 사용. 기본적으로 웹캠이 달려있으면 0, 하나 더 있으면 1 ... 늘려가면서

vc = cv2.VideoCapture("./ch20/turtle.mp4")

while True:
    # vc.read()를 하면 bool 과 영상을 반환함.
    ret, frame = vc.read()
    if not ret:
        break


    edges = cv2.Canny(frame, 100, 200)

    # cv2.imshow("Loaded Image", frame) # 단순히 동영상 재생
    cv2.imshow("Loaded Image", edges) # 단순히 동영상 재생

    
    # waitkey는 키 입력을 감지하여 정수값 반환 / # 대기시간(1ms)
    if cv2.waitKey(1) == ord('q'): 
        break
    
    # waitkey = 1000/FPS      # 1배속 설정 FPS는 어떻게? 동영상에서 봐야 한다는듯
    


vc.release() # 자원 반납. / 비디오 장치 사용 후 자원을 해제

# cv2.imshow("VideoCapture", vc)
# cv2.waitKey(0) # 0: 무한대기

cv2.destroyAllWindows() # 모든 OpenCV 창 닫기


