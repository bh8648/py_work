# file_add.py

path='ch12/file1.txt'
f = open(path, 'a', encoding='utf-8')

for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)

f.close()


