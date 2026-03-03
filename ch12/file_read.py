# file_read.py

# path = 'ch12/file1.txt'
# f = open(path, 'r', encoding='utf-8')

# lines = f.readlines()
# for line in lines:
#     print(line, end="")

# f.close()





path = 'ch12/file1.txt'
f = open(path, 'r', encoding='utf-8')

data = f.read()
print(data)

f.close()



