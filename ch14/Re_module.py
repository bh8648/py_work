# Re_module.py
"""
<축약 전 형태>
패턴객체 = re.compile("[a-z]+")
매치객체 = 패턴객체.match("python")

<축약 후 형태>
매치객체 = re.match('정규표현식', '검색대상문자열')
"""

import re

p = re.compile("[a-z]+")
m = p.match("python")
print(m) # python

print('==============================')

m = re.match("[a-z]+", 'python')
print(m) # python

m = re.match("[a-z]+", 'python', re.I)
print(m) # python