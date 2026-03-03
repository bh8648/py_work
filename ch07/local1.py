# local1.py
b = 0 # 초기화
print("b값", b)
b = 1 # 할당
print("b값", b)

def scope_test():
    a = 1
    print("함수 내 a값:",a)
a = 0
print("함수 밖 a값:",a)
scope_test()
print("함수 호출 후 a값:",a)