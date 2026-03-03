# local3.py

# global 키워드
# 1. 지역변수 -> 전역변수
# 2. 같은 이름의 지역변수 생성 억제
#

b = 0 # 초기화
print("b값", b)
b = 1 # 할당
print("b값", b)

def scope_test():
    global a
    a = a+3
    print("함수 내 a값:",a)

a = 0
print("함수 밖 a값:",a)
scope_test()
print("함수 호출 후 a값:",a)


print("------------------------")


b = 0 # 초기화
print("b값", b)
b = 1 # 할당
print("b값", b)

def scope_test():
    a = 0
    a = a+3
    print("함수 내 a값:",a)
    return a

a = 1
print("함수 밖 a값:",a)
scope_test()
print("함수 호출 후 a값:",a)

