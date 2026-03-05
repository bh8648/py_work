# try_except1.py
# except 절은 여러 개가 존재할 수 있다.
# 또한, except 절은 여러 예외를 괄호로 묶은 튜플로 명명 가능 except (RuntimeError, TypeError, NameError):
# except Exception as e: 처럼 예외 정보는 except 절의 예외 이름 뒤 변수를 as로 지정하여 확인 가능.
# except 구문은 if문처럼 먼저 처리된 것만 실행됨

print("try_except Start3")
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except : # 모든 예외(Base Exception)를 다 처리
        print("Oops! That was no valid number. Try Again.")
    finally:
        print("try or except 실행 시, 무조건 실행")

print("Program Exit")

# except: (모든예외처리)작성시 아래와 같은 예외까지 처리하므로 강제 종료시, 종료가 안될 수 있음.
# KeyboardInterrupt(Ctrl+c)
# SystemExit(프로그램 종료) 같은

# ================================================================

# print("try_except Start1")

# while True:
#     x = int(input("Please enter a number: "))
#     break

# print("Program Exit")

# ================================================================

# print("try_except Start2")
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try Again.")
#     finally:
#         print("try or except 실행 시, 무조건 실행")

# print("Program Exit")


