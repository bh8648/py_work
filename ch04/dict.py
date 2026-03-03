my_dict = {}
my_dict['Name'] = 'James'
my_dict['Age'] = 30
my_dict['Sex'] = 'Male'
my_dict['Hobby'] = ['수영', '독서']

print(my_dict['Age'])
my_dict['Age'] = 29
print(my_dict['Age'])

print("-----------------------")
a = my_dict.get('Name')
print(a)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(type(my_dict.keys()))

aa = my_dict.keys() # 접근안됨.
bb = list(my_dict.keys()) # 리스트로 바꾸면 접근 가능.

print(bb)
print("-----------------------")
c = my_dict.popitem()
print(c)
print(my_dict)
d = my_dict.pop('Age')
print(d)
print(my_dict)


print("-------------------------------")
print()
print()
icecreams = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
icecreams['죠스바'] = 1200
icecreams['월드콘'] = 1500
print(icecreams)

print()
print()

icecreams['메로나'] = 1300
print(icecreams)

print()
print()



