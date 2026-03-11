# 5주차과제.py

# 문제 2: 회전 큐 구현 
#  데이터를 양방향으로 삽입하거나 제거할 수 있는 회전 큐를 구현하시오. 
# • 덱 사용 
# • 리스트로 구현 
# • 왼쪽으로 2만큼 회전 
# import collections
# dq = collections.deque()
# dq.append(1)
# dq.append(2)
# dq.append(3)
# print(dq)
# dq.appendleft(4)
# print(dq)
# num = 2
# for _ in range(num):
#     dq.append(dq[0])
#     dq.popleft()
# print(dq)

# 6. 리스트를 이용하여 기본적인 스택(stack)을 구현하세요. (다음 내용을 고려할 것.)
# push(x): 정수 x를 스택에 삽입
# pop(): 스택에서 가장 위의 값을 제거하고 반환. 만약 스택이 비어 있다면 -1을 반환
# top(): 스택의 가장 위에 있는 값을 반환. 만약 스택이 비어 있다면 -1을 반환
# is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환

# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def push(self, data):
#         self.stack.append(data)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return -1

#     def top(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         return -1
    
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False
    
#     def status(self):
#         return self.stack

# st = Stack()
# print(st.is_empty())
# x = 1; st.push(x); print(st.status())
# x = 2; st.push(x); print(st.status())
# print(st.pop()); print(st.status())
# x = 3; st.push(x); print(st.status())
# print(st.top())
# print(st.is_empty())


# 7. 후위 표기법(Postfix Notation, Reverse Polish Notation)으로 주어진 수식을 계산하는 프로그램을 작성하세요.
# 후위 표기법에서는 연산자가 피연산자 뒤에 위치합니다. 예를 들어, 3 4 +는 3 + 4를 의미하며, 결과는 7입니다.
# 연산자는 +, -, *, /만 고려합니다. (복수 연산자도 처리 가능해야 함.)

# st = []
# data = '3 4 + 6 5 - *'
# data = data.split(" ")
# for x in data:
#     if x in "+-*/":
#         n1 = int(st[-2])
#         n2 = int(st[-1])
#         del st[-2:]
#         if x == "+": st.append(n1+n2)
#         elif x == "-": st.append(n1-n2)
#         elif x == "*": st.append(n1*n2)
#         elif x == "/": st.append(n1/n2)        
#     else:
#         st.append(x)
# print(st[0])


# 8. 리스트를 사용하여 기본적인 큐(queue)를 구현하세요. (다음 내용을 고려할 것.)
# enqueue(x): 정수 x를 큐의 끝에 추가
# dequeue(): 큐의 앞에서 값을 제거하고 반환. 만약 큐가 비어 있다면 -1을 반환
# front(): 큐의 앞에 있는 값을 반환. 만약 큐가 비어 있다면 -1을 반환
# is_empty(): 큐가 비어 있으면 True, 아니면 False를 반환

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         if self.is_empty():
#             return -1
#         return self.queue.pop(0)
#     def front(self):
#         if self.is_empty():
#             return -1
#         return self.queue[0]
#     def is_empty(self):
#         if len(self.queue) == 0:
#             return True
#         return False
#     def status(self):
#         return self.queue

# q = Queue()
# print(q.is_empty())
# x = 1; q.enqueue(x); print(q.status())
# x = 2; q.enqueue(x); print(q.status())
# x = 3; q.enqueue(x); print(q.status())
# print(q.dequeue(), end=" "); print(q.status())
# x = 4; q.enqueue(x); print(q.status())
# print(q.front())
# print(q.is_empty())


# 9. 앞서 작성한 큐 클래스를 활용하여 은행에 도착한 고객 순서대로 업무를 처리하는 선입선출(FIFO) 구조의 큐 프로그램을 작성하세요. 리스트를 활용하여 아래 기능을 수행하는 코드를 작성하세요. (다음 조건을 고려할 것.)
# 조건:
# 1. 고객이 도착하면 이름을 큐에 추가합니다 (Enqueue). 
# 2. 업무 처리가 시작되면 가장 먼저 온 고객부터 이름을 출력하고 큐에서 제거합니다 (Dequeue). 
# 3. 현재 대기 중인 고객 명단을 확인하는 기능을 포함하세요.

# 실행 결과 예시)
# 현재 대기열: ['김철수', '이영희', '박민수']   
# 업무 처리 중인 고객: 김철수
# 남은 대기 고객: ['이영희', '박민수']



# q = Queue()
# condition = True
# while condition:
#     customer = input("도착 고객 이름(종료 -1):")
#     if customer == "-1":
#         break
#     q.enqueue(customer)

# print(f"현재 대기열: {q.status()}")
# print(f"업무 처리 중인 고객: {q.dequeue()}")
# print(f"남은 대기열: {q.status()}")


# 10. 리스트를 이용하여 덱(deque, 양방향 큐)을 구현하세요. (다음 내용을 고려할 것.)
# push_front(x): 정수 x를 덱의 앞에 추가
# push_back(x): 정수 x를 덱의 뒤에 추가
# pop_front(): 덱의 앞에서 값을 제거하고 반환 (비어 있다면 -1)
# pop_back(): 덱의 뒤에서 값을 제거하고 반환 (비어 있다면 -1)

class Deque:
    def __init__(self):
        self.deque = []
    def push_front(self,data):
        self.deque.insert(0, data)
    def push_back(self,data):
        self.deque.append(data)
    def pop_front(self):
        if self.is_empty():
            return -1
        return self.deque.pop(0)
    def pop_back(self):
        if self.is_empty():
            return -1
        return self.deque.pop(-1)
    def is_empty(self):
        if len(self.deque) == 0:
            return True
        return False
    def status(self):
        return self.deque

dq = Deque()
print(dq.is_empty())
dq.push_front(1); print(dq.status())
dq.push_front(2); print(dq.status())
dq.push_back(3); print(dq.status())
dq.pop_front(); print(dq.status())
dq.pop_back(); print(dq.status())
print(dq.is_empty())



