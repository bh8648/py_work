# Re_option.py

import re

"""
1. DOTALL, S
-> 개행문자(\n)도 포함하여 매치하고 싶다면
"""
p = re.compile("a.b")
print(p.match("a\nb")) # None
p = re.compile("a.b", re.DOTALL)
print(p.match("a\nb")) # 'a\nb'
p = re.compile("a.b", re.S)
print(p.match("a\nb")) # 'a\nb'
print("==========================================")
"""
2. IGNORECASE, I
-> 대소문자 구분 없이 문자만 보고 매칭
"""
p = re.compile("[a-z]+")
print(p.match("python")) # python
print(p.match("Python")) # None
print(p.match("PYTHON")) # None

p = re.compile("[a-z]+")
print(p.match("python")) # python
p = re.compile("[a-z]+", re.IGNORECASE)
print(p.match("Python")) # Python
p = re.compile("[a-z]+", re.I)
print(p.match("PYTHON")) # PYTHON
print("==========================================")
"""
3. MULTILINE, M
-> 문자열에 개행 문자(\n)가 포함된 경우, ^, $ 메타 문자의 동작 방식을 변경함 
• 메타문자 ^는 문자열의 처음, $는 문자열의 마지막을 의미 
• ^ 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우, re.MULTILINE 또는 re.M 사용
"""
p = re.compile("^python\s\w+") # 대상 문자열이 python이라는 문자열로 시작하고 그 뒤에 화이트스페이스, 그 뒤에 단어가 와야 한다는 의미 
data = """python one 
life is too short 
python two 
you need python 
python three""" 
print(p.findall(data)) # findall로 찾아도 ['python one'] 1개뿐. Why? ^ 메타 문자에 의해 python 문자열을 사용한 첫 번째 줄만 매치

p = re.compile("^python\s\w+", re.M)
print(p.findall(data)) # ['python one', 'python two', 'python three']
print("==========================================")
"""
4. VERBOSE, X
-> 정규식은 일반적으로 복잡하므로 주석 또는 줄 단위로 구분하면 가독성이 좋음. 이 경우, re.VERBOSE 또는 re.X 옵션을 사용 가능
예) re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);') 
    &: 문자 엔티티의 시작을 나타냄 (HTML 엔티티는 &로 시작) 
    » [#]: # 문자를 문자 그대로 매칭 
    » 숫자 기반의 문자 참조(8진수, 10진수, 16진수)에 사용 
    » & 뒤에 #이 오고 나서, 8진수, 10진수, 16진수 형식 중 하나가 올 수 있도록 패턴이 맞춰짐 

(0[0-7]+|[0-9]+|x[0-9a-fA-F]+) 이 부분은 3가지 옵션 중 하나를 매칭
    » 0[0-7]+: 8진수 문자 참조 (예: &#0123;) 
    » 0: 8진수는 반드시 0으로 시작해야 합니다. 
    » [0-9]+: 10진수 문자 참조 (예: &#123;) 
    » x[0-9a-fA-F]+: 16진수 문자 참조 (예: &x41;) 
    » x: 16진수는 x로 시작합니다.

;는 문자 엔티티의 끝을 나타냄 (HTML 엔티티는 항상 ;로 끝나므로 이를 매칭)
"""
p = re.compile("^python\s\w+") # 대상 문자열이 python이라는 문자열로 시작하고 그 뒤에 화이트스페이스, 그 뒤에 단어가 와야 한다는 의미 

p= re.compile(r""" 
              &[#]
              (
              0[0-7]+
              | [0-9]+
              | x[0-9a-fA-F]+
              )
              ;
              """, re.VERBOSE) # 정규표현식이 복잡하면 이렇게 주석 표시 및 여러 줄 표현이 더 가독성이 좋음
# re.VERBOSE 옵션을 사용하면 문자열에 사용된 화이트스페이스는 컴파일할 때 제거됨 (단, [ ] 안에 사용한 화이트스페이스는 제외)

data = "&#07; &#8; &#x0A;"
print(p.findall(data)) # ['07', '8', 'x0A']



