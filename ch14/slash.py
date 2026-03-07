# slash.py

import re
"""
패턴객체 = re.compile("정규표현식")
패턴객체.match("검색대상문자열")
"""
p = re.compile("\section")
m = p.match("\section python hello thanks")
print(m) # None

p = re.compile("\\section")
m = p.match("\section python hello thanks")
print(m) # None

p = re.compile("\\\\section")
m = p.match("\section python hello thanks")
print(m) # \\section

p = re.compile(r"\\section") # raw string 사용
m = p.match("\section python hello thanks")
print(m) # \\section

# 파이썬 리터럴 규칙 때문에
# "\\" -> "\"
# "\\\\" -> "\\"


import re

text = "Python 파이썬 123 한글"
p = re.compile("[가-힣]")
print(p.findall(text))

