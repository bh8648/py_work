# generator1.py

"""
이터레이터를 생성하는 함수
-> 제너레이터로 생성한 객체는 이터레이터와 마찬가지로 next 함수 호출 시 그 값을 차례대로 획득 가능
-> 제너레이터에서는 차례대로 결과를 반환하고자 return 대신 yield 키워드 사용 (yield: 생성하다)
"""
def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
"""
mygen 함수는 yield 구문을 포함하므로 제너레이터다.
제너레이터 객체는 g=mygen()과 같이 제너레이터 함수를 호출하여 생성됨
"""

print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration

for item in g:
    print(item)

print("=============================================================================================")

def mygen():
    for i in range(1, 101):
        result = i*i
        yield result

gen = mygen()
for x in gen:
    print(x)

