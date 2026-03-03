# continue1.py

# cnt = 0
# while cnt < 3:
#     cnt += 1
#     if cnt == 2:
#         continue
#     print(cnt)




for x in range(101):
    if x % 3 == 0:
        print(x)

print('------------')
n = 10
print((n*(n+1))/2)

n = int(input('총합을 구하려는 수를 입력하세요.'))
total = 0
for x in range(1, n+1):
    total += x
print(f"1부터 {n}까지의 총합은 {total} 이다.")


