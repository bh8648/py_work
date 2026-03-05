# map_func.py
# map 함수
# 리스트나 튜플 등의 반복 가능한 객체의 각 요소에 대해 지정된 함수를 적용하여 그 결과를 새로운 이터레이터로 반환하는 함수.

# map(함수명, 이터러블 객체)
# 예시) numbers 리스트의 각 요소에 square() 함수를 적용
def square(x):
    return x**2

numbers=[1,2,3,4,5]
squared_numbers = map(square, numbers)
print(squared_numbers)
print(list(squared_numbers))

print("==================================================")
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

print("==================================================")
num_list = ["010", 1234, "5678"]
# str(1234)
# joined_string = "-".join(num_list) # TypeError
print(map(str, num_list))
print(list(map(str, num_list)))

joined_string = "-".join(map(str, num_list))
print(joined_string)





