# for _ in range(3) :
#     num = float(input("숫자를 입력하세요 > "))

#     if num.is_integer() :
#         if num % 2 == 0:
#             print("짝수입니다.")    
#         else:
#             print("홀수입니다.")
#     else:
#         print("짝수/홀수를 판별할 수 없습니다.")

# from datetime import datetime

# for _ in range(2):
#     t = input(">> 현재시간: ")
#     t = datetime.strptime(t, "%H:%M")
#     if t.minute == 0:
#         print("정각 입니다.")
#     else:
#         print("정각이 아닙니다.")

try :
    score = int(input("score: "))
except ValueError:
    print("정수를 입력하시오")

if score > 100 or score < 0 :
    print("점수의 범위를 입력하시오(0~100)")
else:
    if score > 80 :
        grade = 'A'
    elif score > 60:
        grade = 'B'
    elif score > 40:
        grade = 'C'
    elif score > 20:
        grade = 'D'
    else:
        grade = 'E'
    print(f'grade is {grade}')
