# week.py

text = "영어로 치환하고 싶은 요일을 입력하시오(예시:월요일) >> "
yoil_kor = input(text)
yoil_dict = {'월요일':'monday', '화요일':'tuesday', '수요일':'wednesday','목요일':'thirsday',
             '금요일':'friday', '토요일':'saturday', '일요일':'sunday'}
print(yoil_dict[yoil_kor])

id = 'abc123'
pw = 1234
id_use = input("id 입력 >")
pw_use = input("pw 입력 >")
id_check = False
pw_check = False

if id == id_use :
    id_check = True
    print("id 일치")
if pw == pw_use :
    pw_check = True
    print("pw 일치")

if id_check and pw_check :
    print("로그인 성공")
else :
    print("로그인 실패")
