# input_func.py
# sa = input("아무거나 입력하세요.").split()
# print(type(sa))
# print(sa)

# buf = input("나이, 이름, 생년월일 >>").split()
# age = buf[0]
# name = buf[1]
# birth = buf[2]

# print(buf)
# print(name)

# ra = input()
# # rb = input()
# # rc = ra+rb

# # print(ra, rb, rc)
# int(ra)


fa = input("첫 번재 실수:")
fb = input("첫 번재 실수:")
fo = input("연산 기호:")

fa = float(fa)
fb = float(fb)

def operate(a, b, op) :
    return_val = 0
    if op == '+' :
        return_val = a + b
    elif op == '-' :
        return_val = a - b
    elif op == '*' :
        return_val = a * b
    elif op == '/' :
        return_val = a / b
    
    print(return_val)

operate(fa, fb, fo)
