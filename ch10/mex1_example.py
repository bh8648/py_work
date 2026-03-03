# mex1_example.py

import mex1

# mex1.py 클래스 활용
p2 = mex1.Cvalue()
p2.add(11)
p2.add(22)
p2.add(33)
print(p2.lista)
p2.fprint()

# mex1.py 함수 활용
value = mex1.plus(10,20)
print(value)

# mex1.py 변수 활용

# print(mex1.p1.lista)
# mex1.p1.add(4)
# mex1.p1.fprint()

# 메인 모듈은 __main__이 저장됨
# 하위 모듈의 경우, 모듈명이 저장됨
print(__name__) # mex1.py의 내장 변수 여기서 실행하면 __main__ / 다른곳에서 mex1을 import하면 mex1이 됨



