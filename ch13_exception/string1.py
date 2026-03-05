# string1.py
muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))

try:
    muna[0] = 'k'
except TypeError as e:
    print(type(e), e)

munb=["python"]
print(type(munb[0]))

munc=["p","y","t","h","o","n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0]='k'
print(munc)

print("====================================")
# 아스키코드 값
for i in range(0,6,1):
    print(muna[i])

print(ord('a'))
print(chr(97))
print(ord('A'))
print(chr(65))


print("====================================")
# 1. % 연산자 사용
# 2. format() 메서드 사용
# 3. f-string 사용
na = 1
nb = 2
print("na 값 %d 더하기 nb 값 %d의 결과값은 %d 이다."%(na, nb, na+nb))


