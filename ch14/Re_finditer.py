# Re_finditer.py

# <finditer 객체 메서드>
# findall과 기능적으로 동일하나, 그 결과로 반복 가능한 객체(iterator object)를 리턴
# # 반복 가능한 객체가 포함하는 각각의 요소는 match 객체임


import re

p = re.compile("[a-z]+")
result = p.finditer("life is too short")
print(result) # <callable_iterator object at 0x0000022E4F98CE20>

# result는 1. 리스트로 변환하거나 2. for문을 사용해서 확인

# print(list(result))
"""
[
<re.Match object; span=(0, 4), match='life'>,
<re.Match object; span=(5, 7), match='is'>,
<re.Match object; span=(8, 11), match='too'>,
<re.Match object; span=(12, 17), match='short'>
]
"""

for match_obj in result:
    print(match_obj.group(), end=" ")
    print(match_obj.span())

"""
life (0, 4)
is (5, 7)
too (8, 11)
short (12, 17)
"""


