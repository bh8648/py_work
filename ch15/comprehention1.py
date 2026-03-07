# comprehention1.py

# 컴프리헨션

buf = [i**2 for i in range(1, 11) if i%2 == 0]
print(buf)

buf = [i**2+1 for i in range(1, 11) if i%2 == 0]
print(buf)


print("=============================================================================================")
buf2 = [[i,i+1,i+2] for i in range(1, 11) if i%2 == 0]
print(buf2)

buf2 = [{i:i**2} for i in range(1, 11) if i%2 == 0]
print(buf2)

print("=============================================================================================")
buf3 = {i:f"{i}의 제곱은 {i**2}입니다." for i in range(1, 5) if i%2 == 0}
print(buf3)

subjects = ['math', 'english', 'history', 'science']
scores = {subject:0 for subject in subjects}
print(scores)

print("=============================================================================================")

gen = (i*i for i in range(1,11))
print(next(gen))
print(next(gen))
for i in gen:
    print(i)
print(next(gen)) # StopIteration



