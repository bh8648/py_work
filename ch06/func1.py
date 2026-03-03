# func1.py
# 함수 정의는 호출할 때만 실행
# 호출한 함수 종료시 호출 위치로 되돌아 온다.

# def funca(na, nb):
#     nc = na+nb
#     print(f"{na} + {nb} = {nc}")

# funca(10, 11)
# funca(20, 21)
# funca(30, 31)


# def fPlusMinus(num):
#     n = num
#     if n == 0 :
#         return "zero", n
#     elif n > 0 :
#         return "plus", n
#     elif n < 0 :
#         return "minus", n

# print(fPlusMinus(0))
# print(fPlusMinus(1))
# print(fPlusMinus(-1))

# def myabs(arg):
#     if arg < 0 :
#         result = arg * -1
#     else:
#         result = arg
#     return result

# print(myabs(10))


# def funcb():
#     funca()
#     print(f"b 함수 호출 ")

# def funcc():
#     funcb()
#     print(f"c 함수 호출 ")
# funcc()


# def funca():
#     print(f"a 함수 호출 ")


def fMinus(pa, pb):
    pc = pa-pb
    return pc

na=10
nb=20
nc=fMinus(na,nb)
print(f"{na}-{nb} = {nc}")



def draw_stars(num):
    print('*'*num)
draw_stars(3)
draw_stars(2)
draw_stars(1)


def fadd(pa, pb) -> int:
    pc = pa + pb
    return pc
def fsub(pa, pb):
    pc = pa-pb
    return pc
def fmul(pa, pb):
    pc = pa*pb
    return pc
def fdiv(pa, pb):
    pc = pa/pb
    return pc

print(fadd(100, 3))
print(fsub(100, 3))
print(fmul(100, 3))
print(fdiv(100, 3))