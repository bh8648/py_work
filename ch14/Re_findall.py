# Re_findall.py

# findall 객체 메서드
# 기능: 패턴(예시:[a-z]+)과 매치되는 모든 값을 찾아 리스트로 반환


import re

p = re.compile("[a-z]+")
result = p.findall("life is too short")
print(result) # ['life', 'is', 'too', 'short']
print(p.findall("3 python")) # ['python']
print(p.findall("3py8thon")) # ['py', 'thon']

temp = "".join(p.findall("3py8thon"))
print(temp)

print("=============================================================================")
text = "The mission of the Python Software Foundation"
p = re.compile("Python")
print(p.findall(text)) # ['python']

print("=============================================================================")
p = re.compile("[a-z]*")
print(p.findall("3py8thon")) # ['', 'py', '', 'thon', '']

"|3|p|y|8|t|h|o|n| -> 마지막 |에서도 검사를 하기 때문에 끝위치에 ''가 들어가는 것"

# 빈 문자열 '' 도 매칭됨.
# 3 -> 소문자 없음 -> ''
# py -> 소문자 있음 -> 'py'
# 8 -> 소문자 없음 -> ''
# thon -> 소문자 있음 -> 'thon'
# 끝위치 -> 소문자 없음 -> ''

# + : 최소 1번 이상 반복
# * : 0번 이상(무한대까지) 반복

