# fmax1.py

su=[5,4,7,10,6]
max_n = su[0]
for x in su[1:]:
    if max_n < x:
        max_n = x
print(max_n)





# 포문 정순으로 돌려서 가장 처음 찾는 짝수의 인덱스
# 포문 역순으로 돌려서 가장 처음 찾는 홀수의 인덱스
# 두 값을 찾으면 서로의 인덱스 값을 반환

arr=[3,6,7,4,9,10,13]
f_even_idx = 0
l_odd_idx = -1
f_even_check = False
l_odd_check = False

for i in range(len(arr)):
    if f_even_check and l_odd_check :
        break
    if f_even_check == False:
        if arr[i] %2 == 0:
            f_even_idx = i
            f_even_check = True
    if l_odd_check == False:
        if arr[-(i+1)] % 2 != 0:
            l_odd_idx = -(i+1)
            l_odd_check = True

print(arr)
arr[f_even_idx], arr[l_odd_idx] = arr[l_odd_idx], arr[f_even_idx]
print(arr)

test_dict = {'a':10, 'b':20, 'c':30}
def sum_dict(test_dict):
    total = 0
    for k in test_dict:
        total += test_dict[k]
    return total
print(sum_dict(test_dict))
