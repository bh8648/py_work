# deque_module.py

from collections import deque

dq = deque() # 덱 생성

dq.append(1) # dq 오른쪽에 데이터 넣기
print(dq)
dq.append(2) # dq 오른쪽에 데이터 넣기
print(dq)
dq.appendleft(10)
print(dq)
dq.appendleft(20)
print(dq)
dq.pop() # dq 왼쪽 데이터 제거
print(dq)
dq.popleft()
print(dq)

print(dq.pop())
print(dq.popleft())
print(dq)

print("========================")


def test1(data) :
    stack = []
    result = False

    for c in data:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack: 
                return result
            
            top = stack.pop()

            print(c)
            print(top)
            
            # stack = ["(", "[", "{"] -> 이 순서로 있으면 닫는 괄호는 "}"가 가장 먼저 나와야 함. 근데 }를 만났는데 스택의 top이 {이 아니라면 바로 False
            if (c == ")" and top != "(") or \
            (c == "}" and top != "{") or \
            (c == "]" and top != "["):
                return result
            

    if not stack:
        result = True

    return result

# data = "(a+b)"
# print(test1(data))
# data = "(a+b)]}"
# print(test1(data))
# data = "[{(x+y)+3}-4]"
# print(test1(data))
# data = "[{({}}}{}{]]]][}]}}"
# print(test1(data))
data = "(}}{{"
print(test1(data))
