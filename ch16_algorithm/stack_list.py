# stack_list.py
# 스택 구현: 리스트 활용

# 빈 스택 구현
stack = []

# push 기능 구현
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.append(4)
print(stack)

# pop 기능 구현
a = stack.pop(); print(a, end=" "); print(stack)
a = stack.pop(); print(a, end=" "); print(stack)
a = stack.pop(); print(a, end=" "); print(stack)
a = stack.pop(); print(a, end=" "); print(stack)

# 스택이 비어있는 경우,
if stack ==[]:
    print("is Empty!")

# 스택 꼭대기 값 확인
if stack != []:
    print(f"TOP is {stack[-1]}")


