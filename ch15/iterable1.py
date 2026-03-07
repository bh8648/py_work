# iterable1.py

a = [1,2,3]
try:
    print(next(a))
except Exception as e :
    print(e)

iter_a = iter(a)

# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a)) # StopIteration 발생

for i in iter_a:
    print(i)

# 위에서 iter 객체의 모든 데이터를 봤기 때문에 여기는 비어있음.
# for문은 다음으로 넘어갈 iter 객체의 데이터가 없어도 에러 발생 안함
for i in iter_a:
    print(i) 

next(iter_a) # StopIteration 발생














