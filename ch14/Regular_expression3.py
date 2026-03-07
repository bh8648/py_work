# Regular_expression3.py # search() 함수 / 

import re

# match 함수는 문자열의 처음부터 매치시켜보기 때문에 가장 앞에서 검색해보기도 함
# search 함수: 문자열 전체에서 일치 여부 검색
# findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
# finditer() 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

p = re.compile("hello$") # 문자열 끝이랑 매치
print(p.match("kenneth,hello")) # None
print(p.match("kenneth, hello")) # None
print(p.match("hello,kenneth")) # None
print(p.match("kim,hello. kenneth, hello")) # None
print(p.match("hello")) # 'hello'

print('======================================')
# search 함수: 문자열 전체에서 일치 여부 검색
p = re.compile("hello$") # 문자열 끝이랑 매치 
print(p.search("kenneth,hello")) # 'hello'
print(p.search("kenneth, hello")) # 'hello'
print(p.search("hello,kenneth")) # None
print(p.search("kim,hello. kenneth, hello")) # 'hello'
print(p.search("hello")) # 'hello'

print('======================================')




