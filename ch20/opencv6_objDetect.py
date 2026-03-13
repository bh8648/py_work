# opencv6_objDetect.py

import cv2

# 1. 이미지 파일 읽기
img = cv2.imread("./ch20/people.jpg")

# 2. 얼굴 검출을 위한 모델을 불러오는 경로 확인
# 앞에가 경로 뒤에가 이름+확장자
face_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# 'haarcascade_eye.xml'
# 'haarcascade_russian_plate_number.xml'
# 'haarcascade_car.xml'


# 3. 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 4. 커스케이드 분류기 생성
face_cascade = cv2.CascadeClassifier(filename=face_path)
# Haar Cascade 분류기를 로드하는 OpenCV의 클래스
# 얼굴, 눈, 차량 번호판 등의 객체 검출에 사용
# 학습된 XML 파일을 입력으로 받아 객체를 생성

# filename : 객체 검출을 위한 사전 학습된 Haar Cascade 모델의 경로 이름


faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# scaleFactor : 검색 윈도우 확대 비율(1보다 커야 함) // 이미지 크기를 줄여가며 검출(1.1을 넣으면 10%씩 줄여가면서 검사) // 원근감 등의 이유로 사람 얼굴 크기가 여러개이므로 이미지를 축소하면서 얼굴 탐색
# minNeighbors : 검출 영역으로 선택하기 위한 최소 (중첩)검출 횟수 // 검출된 객체에 대한 최소 인접 사각형 개수 // 대상 객체로 인지되기 위한 최소 중복 검출 수
# minSize: 검출할 객체의 최소 크기 // 최소 바디 크기 // 이 크기보다 작은 객체는 얼굴로 간주 안함
# maxSize: 검출할 객체의 최대 크기
# Sequence[Rect] : (출력) 검출된 객체의 사각형 좌표 정보

print(faces) # [x, y, w, h]

for (x,y,w,h) in faces:
    cv2.rectangle(img, # 사각형을 그릴 이미지
                (x,y), # 좌상단 꼭지점 위치
                (x+w, y+h), # 우하단 꼭지점 위치
                (200,0,0), # 두께
                2)






cv2.imshow("Image", img)
cv2.waitKey(0) # 0: 무한대기
cv2.destroyAllWindows()





