# generator2.py

import time

# def longtime_job():
#     print("job start")
#     time.sleep(1) # 1초 지연
#     return "Done"

# list_job = [longtime_job() for _ in range(5)]

# print(list_job)

print("=============================================================================================")
# 제너레이터 컴프리헨션 (튜플모양으로 컴프리헨션 사용)

def longtime_job():
    print("job start")
    time.sleep(1) # 1초 지연
    return "Done"

list_job = (longtime_job() for _ in range(5)) # 이건 제너레이터 컴프리헨션. 즉 튜플이 아니라 제너레이터다.
# print(list_job) # 실행 시 next 함수 1회 실행에 따른 약 1초의 시간만 소요.

print(next(list_job))
print("컨베이어벨트 청소")
print(next(list_job))
print("재료 준비")
print(next(list_job))
print("기계 상태 확인")
print(next(list_job))
print(next(list_job))
"""
제너레이터 표현식에서 longtime_job()함수는 호출 단계에서 미리 실행 5회가 아닌 next 함수에 따른 결과값이 필요할 때, 1회만 호출
이렇듯 결과값이 필요할 때까지 연산을 늦추는 방식 -> 느긋한 계산법(lazy evaluation)
시간이 걸리는 작업을 한꺼번에 처리하기보다는 필요한 경우에만 호출하여 사용할 때 제너레이터가 유용함
"""






