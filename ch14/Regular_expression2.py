# Regular_expression2.py # .(dot) / * / + / {}

import re

# .문자
p = re.compile(".")
print(p.match("apple")) # 'a'

p = re.compile("a.b")
print(p.match("aab")) # 'a'
print(p.match("a0b")) # '0'
print(p.match("abc")) # None
print(p.match("a\nb")) # None -> 줄바꿈(\n) 문자는 매치가 안됨
print(p.match("a\tb")) # 'a\tb'

p = re.compile("a[.]b")
print(p.match("aab")) # None
print(p.match("a.b")) # 'a.b'

print('=================================')
# *문자
p = re.compile("ca*t")
print(p.match("ct")) # ct
print(p.match("cat")) # cat
print(p.match("caaat")) # caaat

print('=================================')
# +문자
p = re.compile("ca+t")
print(p.match("ct")) # None
print(p.match("cat")) # cat
print(p.match("caaat")) # caaat

print('=================================')
# {}문자
# {m, n}
# {m}
p = re.compile("ca{2}t")
print(p.match("ct")) # None
print(p.match("cat")) # None
print(p.match("caat")) # 'caat'
print(p.match("caaat")) # None
print()
p = re.compile("ca{2,}t")
print(p.match("ct")) # None
print(p.match("cat")) # None
print(p.match("caat")) # 'caat'
print(p.match("caaat")) # 'caaat'
print()
p = re.compile("ca{,2}t")
print(p.match("ct")) # 'ct'
print(p.match("cat")) # 'cat'
print(p.match("caat")) # 'caat'
print(p.match("caaat")) # None
print()
p = re.compile("ca{1,2}t")
print(p.match("ct")) # None
print(p.match("cat")) # 'cat'
print(p.match("caat")) # 'caat'
print(p.match("caaat")) # None
print()
p = re.compile("ca{,}t") # {,}는 0회 이상 무한대까지 이므로 *과 똑같이 동작함
print(p.match("ct")) # 'ct'
print(p.match("cat")) # 'cat'
print(p.match("caat")) # 'caat'
print(p.match("caaat")) # 'caaat'

print('=================================')
# ?문자
p = re.compile("ca?t") # {0, 1}
print(p.match("ct")) # 'ct'
print(p.match("cat")) # 'cat'
print(p.match("caat")) # None
print(p.match("caaat")) # None

print('=================================')
# ^(캐럿) 문자
p = re.compile("^hello") # 문자열의 시작과 매치
print(p.match("kenneth,hello")) # None
print(p.match("hello,kenneth")) # 'hello'

print('=================================')
# $ 문자
p = re.compile("hello$") # 문자열 끝이랑 매치 / match 함수는 문자열의 처음부터 매치시켜보기 때문에 가장 앞에서 검색해보기도 함
print(p.match("kenneth,hello")) # None
print(p.match("kenneth, hello")) # None
print(p.match("hello,kenneth")) # None
print(p.match("kim,hello. kenneth, hello")) # None
print(p.match("hello")) # 'hello'


