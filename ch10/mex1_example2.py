# mex1_example2.py

from mex1 import plus
from mex1 import Cvalue
from mex1 import p1

value = plus(10,20)
print(value)

p3 = Cvalue()
print(p3.lista)
p3.add("사과")
p3.add("배")
p3.fprint()

p1.add(5)
print(p1.lista)


# 메인 모듈은 __main__이 저장됨
# 하위 모듈의 경우, 모듈명이 저장됨
print(__name__)   # mex1.py의 내장 변수 여기서 실행하면 __main__ / 다른곳에서 mex1을 import하면 mex1이 됨



# 파이썬 모듈 임포트시 특정 클래스, 함수, 변수를 명시하는 이유
# 1. 코드 간결화(가독성)
# 2. 네임스페이스 충돌 방지
# 3. 기능 사용의 명확성
# 단, 실행 성능 차이는 거의 없음