# mex4.py

class Cvalue:
    def __init__(self):
        self.lista=[]
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

def plus(a,b):
    c = a+b
    return c

# 메인 모듈은 __main__이 저장됨
# 하위 모듈의 경우, 모듈명이 저장됨
print(__name__) # print(__name__)  # mex1.py의 내장 변수 여기서 실행하면 __main__ / 다른곳에서 mex4을 import하면 mex1이 됨

if __name__=="__main__":
    # 객체(변수) 생성
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()

    


