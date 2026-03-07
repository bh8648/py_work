# 4주차숙제.py



# path = "./pizza_file1.txt"
# data = """페퍼로니피자 3000
# 치즈피자 3200
# 콤비네이션피자 3500
# """
# additinal_data = """불고기피자 3600
# 해산물피자 3800
# """
# with open(path, 'r', encoding="UTF-8") as f:
#     lines = f.readlines()
#     pizza_list = []
#     for line in lines:
#         pizza_name_and_price = line.split()
#         pizza_list.append(pizza_name_and_price[0])

# print(pizza_list)



try:
    raise KeyError
except KeyError as e:
    print("Key is missing!")



add = lambda x,y:x+y
print(add(3,5))


per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))    
    except ValueError as e:
        print(0)

# for _ in range(3):
#     numbers = [10, 20, 30]
#     try:
#         i = int(input("인덱스 입력: "))
#         print(numbers[i])
#     except IndexError as e:
#         print("잘못된 인덱스입니다.")
#     except ValueError as e:
#         print("정수를 입력하세요.")

import re
pattern = r'\w+'
text = "Hello, World!"
print(re.findall(pattern, text))


import re
pattern = r'(ab)+'
text = "ababab"
match = re.match(pattern, text)
print(match.group())



import re
text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
p = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
m = p.findall(text)
print(m)

import re
text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
p = re.compile(r"010-\d{4}-\d{4}")
m = p.findall(text)
print(m)



# 처음 [^.]*은 .를 문장단위로 끊을 수 있게 .이 아닌 문자가 하나라도 있으면 거기부터 시작함
# 두 번째 [^.]*은 Python이 중간에 적혀있을 경우
# 마지막 \.을 통해 문장 단위로 끊어냄
import re
text = "I love Python. Java is also popular. Python is great for AI."
p = re.compile(r"[^.]*Python[^.]*\.") 
m = p.findall(text)
result = [x.strip() for x in m]
print(result)

# 숫자만 찾기
import re
text = "상품 코드: A123, B456, C789, 가격: 12000원"
p = re.compile(r"\d+") 
m = p.findall(text)
print(m)

# 연속된 대문자만 찾기 ex) NASA, AI
import re
text = "NASA is working on AI projects with IBM and Google."
p = re.compile(r"[A-Z]{2,}") 
m = p.findall(text)
print(m)




numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
for x in iter_numbers:
    print(x)


fruits = ["apple", "banana", "cherry"]
iter_fruits = iter(fruits)
try:
    while True:
        print(next(iter_fruits))
except StopIteration as e :
    print("StopIteration")


q8_iterator = (x for x in range(10))
for x in q8_iterator:
    print(x**2)

q9_iterator = (x for x in range(11))
for x in q9_iterator:
    if x %2 == 0:
        print(x)


class MyRange:
    def __init__(self, start, stop = None, step=1):
        if stop == None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop        
        if step == 0:
            raise ValueError("arg 3 must not be zero")
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0 :
            if self.start >= self.stop:
                raise StopIteration
        else:
            if self.start <= self.stop:
                raise StopIteration        
        result = self.start
        self.start += self.step
        return result

def test_my_iterator(my_iterator):
    try:
        while True:
            print(next(my_iterator))
    except StopIteration:
        print("====STOP====")

test_my_iterator(MyRange(3))
test_my_iterator(MyRange(10, 13))
test_my_iterator(MyRange(3, 0, -1))



with open("data.txt", 'w', encoding='utf-8') as file:
    for i in range(1, 11):
        file.write(f"{i}번째 줄입니다.\n")
print("파일이 성공적으로 작성되었습니다.")
with open("data.txt", 'r', encoding='utf-8') as file:
    contents = file.read()
print("파일내용:")
print(contents)


with open("data.txt", 'a', encoding="utf-8") as file:
    file.write("11번째 줄입니다.\n")
with open("data.txt", 'r', encoding='utf-8') as file:
    contents = file.read()
print("파일내용:")
print(contents)




# 문제 1) 예외처리를 이용해 다음 조건을 만족하는 프로그램을 작성하시오.
# 	1. 사용자로부터 숫자를 입력받아 제곱값을 출력
# 	2. 숫자가 아닌 값을 입력하면 “올바른 숫자를 입력하세요!”라는 메시지를 출력하고,
# 	   올바른 숫자가 입력될 때 까지 반복

# condition = True
# while condition :
#     try:
#         num = float(input("숫자를 입력하세요: "))
#         print(num**2)
#         condition = False
#     except ValueError as e:
#         print("올바른 숫자를 입력하세요!")

    

# 문제 2) map() 함수와 람다 함수를 사용해 리스트 [10, 20, 30, 40, 50]의 각 요소를 제곱한 결과를 출력하는 프로그램을 작성하시오.

temp = [10,20,30,40,50]
result = list(map(lambda x:x**2, temp))
for x in result:
    print(x)



# 문제 1) 주어진 문자열에서 python으로 시작하는 모든 문장을 찾아 출력하는 프로그램을 작성하시오.
data = """python one
life is too short
python two
you need python
python three"""

import re
p = re.compile(r"^python\s+\w+", re.M)
m = p.findall(data)
print(m)


# 문제 2) 사용자로부터 이메일 주소를 입력받고, 올바른 이메일 형식인지 검증하는 프로그램을 작성하시오.
# 이메일 형식: user@example.com

# import re
# condition = True
# while condition:
#     try:
#         email = input("이메일 주소를 입력하세요.:")
#         p = re.compile(r"\w+@\w+\.\w+")
#         m = p.match(email).group()
#         print(m)
#         condition = False
#     except AttributeError as e:
#         print("올바른 형식이 아닙니다.")


# 문제 2) 제너레이터 함수를 만들어 1부터 n까지 숫자의 제곱을 생성하는 프로그램을 작성하시오.

class MyIterator:
    def __init__(self, end_num):
        self.start_num = 1
        self.end_num = end_num
    def __iter__(self):
        return self
    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration
        result = self.start_num**2
        self.start_num += 1
        return result

test_iterator = MyIterator(5)
print(next(test_iterator)) # 1
print(next(test_iterator)) # 4
print(next(test_iterator)) # 9
print(next(test_iterator)) # 16
print(next(test_iterator)) # 25
# print(next(test_iterator)) # StopIteration





