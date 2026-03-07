# Re_match.py

# match 객체 메서드
# 기능: 매치된 문자열 및 인덱스 확인 가능

# match 객체란 p.match, p.search 또는 p.finditer 메서드에 의해 리턴 된 객체를 의미함.

# group : 매치된 문자열을 리턴한다
# start: 매치된 문자열의 시작 위치를 리턴한다.
# end: 매치된 문자열의 끝 위치를 리턴한다.
# span 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.


import re

p = re.compile("[a-z]+")
m = p.match("python")
print(m) # python

print(p.match("3python")) # None # 문자3이 정규식에 부합하지 않으므로 None 리턴
print(p.match(" python")) # None
print(p.match("3 python")) # None

print("=============================================================================")

p = re.compile("[a-z]+")
m = p.match("python")
if m:
    print(f"match found: {m.group()}")
else: # 매칭된게 없으면 실행
    print("No match")

print("=============================================================================")
print(m)
print(m.group())
print(m.span())
print(m.start())
print(m.end())


