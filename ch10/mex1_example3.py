# mex1_example3.py
# from 모듈명 import *

from mex1 import *

value = plus(10,20)
print(value)

p4 = Cvalue()
print(p4.lista)
p4.add("목련")
p4.add("장미")
p4.fprint()

p1.add(6)
print(p1.lista)


# 메인 모듈은 __main__이 저장됨
# 하위 모듈의 경우, 모듈명이 저장됨
print(__name__)   # mex1.py의 내장 변수 여기서 실행하면 __main__ / 다른곳에서 mex1을 import하면 mex1이 됨