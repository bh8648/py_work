# try_except2.py


# path = "ch13_exception/myfile.txt"
# mode = 'w'
# encoding = 'UTF-8'
# f = open(path, mode)
# f.close()
# mode = 'r'
# f = open(path, mode)
# f.close()
# s = f.readline()
# # i = int(s.strip())
# i = s.strip()

# print(i)
# f.close()

# FileNotFoundError
# ValueError

print("-----------------------------------")
path = "ch13_exception/myfile.txt"
try:
    f = open(path)    
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
# except ValueError:
#     print("정수형으로 변환 불가")
except Exception as e:
    print("예외 발생!")
    print(e)
finally:
    try:
        f.close()
    except NameError:
        pass

# except 구문은 if문처럼 먼저 처리된 것만 실행됨

print('program exit')