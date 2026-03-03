# class1.py

# # 클래스 정의
# class 클래스명:
#     #멤버변수
#     변수명 = 데이터값
#     #멤버 함수(=메서드)
#     def 함수명(self, 매개변수, 등등):
#         #멤버 변수
#         self.변수명 = 데이터값
#         return 반환값

# # 객체 생성(생성자함수 사용)
# 객체변수명 = 클래스명()

# # 객체 접근
# 객체변수명.변수명
# 객체변수명.함수명(인수1, ...)


# class Pizzaclass:
#     # 멤버 함수(=메서드): 주문하다
#     def __init__(self, kind):
#         self.kind = 30
#     def order(self):
#         # 멤버변수
#         self.kind = 40
        

# combo = Pizzaclass(20)
# print(combo.kind)

class Pizzaclass:
    # 멤버 함수(=메서드): 주문하다
    def order(self):
        # 멤버변수
        self.kind = 40
        

combo = Pizzaclass()
combo.order()
print(combo.kind)

potato = Pizzaclass()
potato.order()
print(potato.kind)


# 클래스 정의
class Singer:
    # (클래스) 멤버 변수
    name = "아이유"
    def sing(self):
        self.name="아이유2" # (인스턴스)멤버변수
        # print(self.name)
        print("가사 내용 1234~")

# 객체 생성(생성자 함수 활용)
iu = Singer()
print(Singer.name) # 클래스 멤버 변수 접근
iu.sing() # 객체 기능/동작 호출
print(iu.name) # 인스턴스 멤버 변수 접근


print("==========================")
bts = Singer()
bts.sing()
print(bts.name)