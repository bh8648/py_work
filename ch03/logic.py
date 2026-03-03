print(True and True)
print(False and True)
print(True and False)
print(False and False)

print(not 9>4 or 3<2 and 4>2)
print((3-5)+2<1 and 3*5>1)
print(3<2 == False)

score = -550
if score > 980 or score < 0 :
    print('out of range')
elif score > 900:
    print('상위권')
elif score <= 900 and score > 700 :
    print('중위권')
else:
    print('하위권')
