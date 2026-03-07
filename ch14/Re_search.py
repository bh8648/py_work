# Re_search.py

# search 객체 메서드
# 기능: 컴파일된 패턴객체 p를 사용하여 search 메서드 수행


import re

p = re.compile("[a-z]+")
m = p.search("3 python") # 첫 번째 문자는 "3"이지만 search는 문자열 전체를 검색하기 때문에 "3" 이후의 "python"문자열과 매치
print(m) # python

print("=============================================================================")

text = "The mission of the Python Software Foundation"
p = re.compile("Python")
m = p.search(text)
print(m)


p = re.compile("[a-z]*")
m = p.search("3pyt8hon")
print(m) # '' -> Why? # 아무 것도 없어도 조건 만족(0글자 매칭 가능) 따라서 3 앞에 아무것도 없어서 0부터 매칭됨








