# list_swap1.py


ca = [10, 11]
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])
temp=ca[0]
ca[0]=ca[1]
ca[1]=temp
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])

print("======================")

def funca(na, nb):
    temp = na
    na = nb
    nb = temp
ca = [10, 11]
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])
funca(ca[0], ca[1])
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])

print("======================")
ca = [10, 11]
cb = ca

print("ca 값은", ca, end=" ")
print("cb 값은", cb)

temp=cb[0]
cb[0]=cb[1]
cb[1]=temp
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])
print("cb[0]의 값은",cb[0], "cb[1]의 값은",cb[1])

print("======================")
def funca(cb):
    temp=cb[0]
    cb[0]=cb[1]
    cb[1]=temp
ca=[10, 11]
cb = ca
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])
print("cb[0]의 값은",cb[0], "cb[1]의 값은",cb[1])
funca(cb)
print("ca[0]의 값은",ca[0], "ca[1]의 값은",ca[1])
print("cb[0]의 값은",cb[0], "cb[1]의 값은",cb[1])

print("======================")
a=[10,11,12,13]
print("리스트a의 값", a)

a[1]=21
print("리스트a의 값", a)

b=a
print("리스트b의 값", b)

b=[30,31,32,33]
print("리스트b의 값", b)
print("리스트a의 값", a)
# 원래는 변수 b가 변수 a에 할당된 리스트의 주소와 연결되어있지만
# 위에서 값을 할당시켜서 연결이 끊어짐



