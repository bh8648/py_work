# raise1.py

# raise 예외 클래스명(예외정보데이터)

try:
    raise NameError('Hi There')
except NameError as e:
    print("An exception flew by!")
    print(e)

