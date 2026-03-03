# default2.py

def personc(height, weight, age=22):
    print("함수 기본값 설정")
    print("나이=", age, end=' ')
    print("체중=", weight, end=' ')
    print("신장=", height)
personc(168, 55)

# 키워드 인수 : 이름을 지정해서 전달하는 인수
personc(168, weight=55)
## personc(168, 33, weight=55) # 인수 전달 위치가 안맞아서 에러 발생


# 가변 위치 인자(*args): 개수가 정해지지 않은 인수
def total(*numbers):
    print(numbers)
total()
total(1)
total(1,2)
total(1,2,3)

# 가변 키워드 인자(**kwargs): 이름 붙은 인수를 여러개 받음
def profile(**info):
    print(info)
profile(name='홍길동', age=553, address='한양외곽')

