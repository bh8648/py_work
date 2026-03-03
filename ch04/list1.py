# list1.py


a = []


a.append(1)
a.insert(0, '2')
a.append(1)

print(a)

a.remove(1)

print(a)
a = [x for x in range(10)]
del a[3:6]
print(a)

b = [[22,11,33], [555,444,333]]
a.extend(b)
print(a)


t1 = (1,2) + (3,4)
print(t1)
t2 = (1,2)
t3 = (3,4)
print(t2 + t3)