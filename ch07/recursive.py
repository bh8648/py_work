# recursive.py
# 재귀: 본래 위치로 다시 돌아오는 것.

# 기저 조건(Base case): 재귀 호출을 멈추는 조건
# 재귀 단계(Recursive step) : 


def count_down(n):
    if n == 0:
        print("새해가 밝았습니다!")
        return
    print(n)
    count_down(n-1)

count_down(10)

# 연습문제
x=10
def fadd(num):
    # 함수 내부에서 전역 변수를 '쓰기'는 불가능 하지만 '읽기'는 가능하기 때문
    b=x+num
    print("변수x값은", x)
    print("변수b값은", b)
fadd(10) # 에러가 아니네?


# 연습문제
x=10
def fadd(num):
    x=x+num # 전역 변수를 '쓰기'를 하려고 했기에 에러
    print("변수x값은", x)
# fadd(10) # 에러 


# 연습문제
x=10
def fadd(num):
    global x
    x=x+num
    print("변수x값은", x)
fadd(10)



def add_numbers(a=10, b=20):
    result = a + b
    return result
result = add_numbers()
print(result)


def message() :
    print("A")
    print("B")
message()
print("C")
message()

def check_odd_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_odd_even(4))
print(check_odd_even(7))
        


def calculate_average(num_list):
    a = sum(num_list)
    b = len(num_list)
    return a/b

num_list = [10, 20, 30, 40, 50]
average = calculate_average(num_list)
print("평균: ", average)
