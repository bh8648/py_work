# file_write.py

import os
print(os.getcwd())

# open('경로')
f = open('./ch12/file1.txt', 'a', encoding='UTF-8')
for i in range(1,11):
    data = f"%d번째 줄입니다. \n"%i
    f.write(data)
f.close()






