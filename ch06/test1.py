
# v= [[1,4], [3,4], [3,10]]

# a = [1,3,3]
# print(a.count(3))
# print(a)


# arr = [4,3,2,1]
# print(min(arr))
# arr.remove(min(arr))
# print(arr)

# n = 1144
# print(str(n))
print()
print()
print()
print()
print()
print()
answer = 0
position=[0,0]
first_walk=[]
actions=[]
dirs="LU"
for x in dirs:
    if x =="U":
        actions.append([0,1])
    elif x =="D":
        actions.append([0,-1])
    elif x =="R":
        actions.append([1,0])
    elif x =="L":
        actions.append([-1,0])
print("acition", actions)
for action in actions:
    print("act", action)
    print("pos", position)
    next_position = position.copy()
    next_position[0] = position[0] + action[0]
    next_position[1] = position[1] + action[1]
    print("new_pos", next_position)
    print("111111111111")
    if abs(next_position[0]) <= 5 and abs(next_position[1]) <= 5:
        print("궁금", [position, next_position])
        print("궁금2", [next_position, position])
        print("first_walk1",first_walk)
        if (position, next_position) not in first_walk and (next_position, position) not in first_walk:
            print("2222222222")
            print([position, next_position])
            print("first_walk2",first_walk)
            first_walk.append((position, next_position))
            print("first_walk3",first_walk)
            position = next_position
            print("first_walk4",first_walk)


print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

result = []
enroll = ['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young']
referral = ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward']
seller = ['young', 'john', 'tod', 'emily', 'mary']
amount =[12,4,2,5,10]

result = dict()

for x in enroll:
    result[x] = 0
print(result)
for i, v in enumerate(amount):
    profit = 100*v
    result[seller[i]] += (profit-int(profit*0.1)) # young은 1080수익
    for j, name in enumerate(enroll): # 등록인원 전체 조회
        if name == seller[i]: # 등록인원 중 young을 만났다면
            refer_name = referral[j]  # 영의 레퍼럴을 찾기. 여기선 edward.    
            refer_fee = int(profit*0.1)
            while refer_name != '-' and (refer_fee > 1): # 레퍼럴이 없는 사람을 만날때까지 계속 반복
                result[refer_name] += refer_fee # 레퍼럴한테 1할 주기. 120에서 12를 빼서 줘야 함
                result[refer_name] -= int(refer_fee*0.1)
                refer_fee = int(refer_fee*0.1) # 다음에 줄 일 있으면 그건 1할의 1할

                for k, name in enumerate(enroll): # 등록인원 전체 조회
                    if name == refer_name: # edward(레퍼럴)를 만났다면
                        refer_name = referral[k] # refer_name = edward(레퍼럴)의 레퍼럴.
        
    


print(result)
answer = list(result.values())

