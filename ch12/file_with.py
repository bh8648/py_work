# file_with.py

path='ch12/file1.txt'
mode = 'w'
encoding='utf-8'
# with 구문은 자동 close
with open(path, mode, encoding=encoding) as f:
    f.write("Hi, Bye\n")

mode='a'
with open(path, mode, encoding=encoding) as f:
    f.write("안녕, 잘가\n")

mode='r'
with open(path, mode, encoding=encoding) as f:
    lines = f.readlines()
    for line in lines:
        print(line)


