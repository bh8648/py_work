# Regular_expression1.py # [] 사용
"""
정규표현식(Regular Expression)
문자열의 패턴을 정의해서 "검색, 검사, 치환, 추출" 등을 할 수 있게 해주는
[문자열 처리 규칙]
"""

import re
"""
정규표현식을 정의해서 컴파일 함수 인자로 전달하면
패턴 객체를 반환함.
패턴객체: "검색대상이 되는 문자열"에서 패턴의 발견을 도와주는 객체

패턴객체 = re.compile("정규표현식")
매치객체 = 패턴객체.match("검색대상문자열") # match 함수: 문자열 처음부터 정규식과 매치되는지 조사함
print(매치객체)
"""

# 메타 문자: 별도의 의미가 담겨있는 문자.
# []
# match 함수
p = re.compile("[a]")
m = p.match("banana") # match 함수: 문자열 처음부터 정규식과 매치되는지 조사함
print(m) # None -> why? 검색대상의 가장 앞을 기준으로 찾기 때문.

p = re.compile("[a]")
m = p.match("apple") 
print(m) # <re.Match object; span=(0, 1), match='a'>    # 매치객체가 리턴됨 # span은 검색된 위치가 어디인지

p = re.compile("[ab]") # a 또는 b로 시작되는 문자열 찾기
print(p.match("banana")) # 'b'
print(p.match("apple")) # 'a'

p = re.compile("[a-c]")
print(p.match("a")) # 'a'
print(p.match("before")) # 'b'
print(p.match("dude")) # None

print("----------------------------------------------")
p = re.compile("[ab][ab]") # 첫 글자가 a나 b가 매치되는지 판단하고 두 번째 글자도 a나 b가 매치되는지 판단
print(p.match("banana")) # 'ba'
print(p.match("apple")) # None

p = re.compile("[ba]") # 1 letter(b or a) 매치 여부
p = re.compile("ba") # 2 letter(ba) 매치 여부
print(p.match("banana")) # 'ba'
print(p.match("apple")) # None
print("----------------------------------------------")
p = re.compile("[0-5]")
print(p.match("3banana")) # '3'
print(p.match("7banana")) # None

p = re.compile("[^0-5]") # 0부터 5까지 숫자가 아닌것과 매칭
print(p.match("3banana")) # None
print(p.match("7banana")) # '7'
print(p.match("banana")) # 'b'
print(p.match("^banana")) # '^'
print()
p = re.compile("[\^0-5]") # ^,0,1,2,3,4,5로 시작하면 매칭
print(p.match("3banana")) # '3'
print(p.match("7banana")) # 'None'
print(p.match("banana")) # 'None'
print(p.match("^banana")) # '^'
print()
p = re.compile("[0\-5]") # 0,-,5 로 시작하면 매칭
print(p.match("3banana")) # 'None'
print(p.match("7banana")) # 'None'
print(p.match("-banana")) # '-'

print("----------------------------------------------")
p = re.compile("[a-z]")
print(p.match("apple")) # 'a'
print(p.match("Apple")) # 'None'
print(p.match("banana")) # 'b'
print()
p = re.compile("[a-zA-Z]")
print(p.match("apple")) # 'a'
print(p.match("Apple")) # 'A'
print(p.match("banana")) # 'b'

print("----------------------------------------------")
p = re.compile("[\d]")
print(p.match("1apple")) # '1'
print(p.match("Apple")) # 'None'
print(p.match("banana")) # 'None'

print("----------------------------------------------")
p = re.compile("[\w]")
print(p.match("1apple")) # '1'
print(p.match("Apple")) # 'A'
print(p.match("banana")) # 'b'
print(p.match("_carrot")) # '_'
print()
p = re.compile("[\W]") # [^a-zA-Z0-9_] 같은 결과
print(p.match("1apple")) # 'None'
print(p.match("Apple")) # 'None
print(p.match("banana")) # 'None
print(p.match("_carrot")) # 'None

print("----------------------------------------------")
p = re.compile("[\s]")
print(p.match("apple")) # 'None'
print(p.match(" banana")) # ' '
print(p.match("\tapple")) # '\t'
print(p.match("\nbanana")) # '\n'
