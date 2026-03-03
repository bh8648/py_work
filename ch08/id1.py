# id1.py

a = [10,11,12,130]
print(id(a))
print(id(a[0]))
print(id(a[1])) # 32증가 -> int는 4byte -> 8비트*4 = 32
print(id(a[2])) # 32증가
print("=================")
a[1] = 21
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print("=================")
b=a
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2])) # b=a이므로 a가 가리키는 주소와 연결됨 = a와 결과가 같음
print("=================")
b=[30,31,32,33]
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2])) # b값을 새로 할당했으므로 기존에 연결된 리스트의 주소와 달라짐

