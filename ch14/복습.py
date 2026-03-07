a = "-".join('abcd')
b = a.join("1234") # 1234 사이에 abcd가 삽입됨
c = "-".join(['A','B','C'])
print(a)
print(b) 
print(c)

m = map(int, ["1", "2", "3"])
print(m)            # <map object at 0x...>
print(next(m))      # 1
print(list(m))      # [2, 3]  (이미 1은 소비됨)

print(chr(65))
print(ord('A'))