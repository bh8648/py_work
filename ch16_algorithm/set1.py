# set1.py

s1 = {1,3,2}
s2 = {1, 10, 20}
print(s1)
print(s2)

print(s1.intersection(s2))
print(s1)

s1.intersection_update(s2)
print(s1)

s3 = {3,4,5,6,7}
s4 = {5,6,7,8,9}

s1&s2
s1|s2

print(s3.union(s4))
print(s3-s4)