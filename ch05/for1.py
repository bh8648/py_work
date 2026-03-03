# for1.py

for n in range(10, -1, -1):
    print(n)

stra = '파이썬'
strb = '프로그래밍'
stra += strb
print(stra)


for i in range(1, 5):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()



가격리스트 = [100, 200, 300]
for price in 가격리스트 :
    print(price + 10)


리스트 = ['dog', 'cat', 'parrot']
for c in 리스트 :
    print(f"{c} {len(c)}")



리스트 = ["가", "나", "다", "라"]
for x in 리스트[1:]:
    print(x)

리스트 = [3, -20, -3, 44]
for x in 리스트:
    if x < 0 :
        print(x)


for x in range(2002, 2051, 4):
    print(x)


total_sum = 0
i = 1
while i < 101 :
    total_sum += i
    i += 1
print(total_sum)



odd_nums = []
even_nums = []

for x in range(1, 31):
    if x % 2 == 0 :
        even_nums.append(x)
    else:
        odd_nums.append(x)


print(f"홀수 : {odd_nums}")
print(f"짝수 : {even_nums}")