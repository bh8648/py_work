# func2.py

sta="python example"
def string_length(stb):
    i = 0
    for _ in stb:
        i += 1
    return i

lena=string_length(sta)
print(lena)



# def fdiv():
#     pa = int(input())
#     pb = int(input())
#     try :
#         print(f"{pa} 나누기 {pb}는 {pa/pb}입니다.")
#     except :
#         print("0으로는 나눌 수 없습니다.")

    
# fdiv()


# def test2():
#     num = int(input())
#     total = 0
#     for i in range(101):
#         if i % num == 0:
#             total += i
#     print(total)
# test2()

# print(abs(-5))
print("===========================")

def print_hello():
    print("안녕하세요")
for _ in range(100) :
    print_hello()


def greet(name="Guest"):
    print(f"Hello, {name}!")
name = "Alice"
greet(name)
greet()


Numbers = [1,2,3,4,5]
for x in Numbers:
    print(x)


fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
for x in fruits:
    message = "사과를 찾았습니다!"
    print(x)
    if x == "사과":
        print(message)


def solution(a, b):
    sum = a+b
    sub = a-b
    multi = a*b
    return sum, sub, multi
a, b = map(int, input().split())
a1, a2, a3 = solution(a, b)
print(a1, a2, a3)


# def test2() :
#     n = int(input("숫자를 입력 > "))
#     total = 0
#     for x in range(1, n+1):
#         total += x
#     return total

# print(test2())

