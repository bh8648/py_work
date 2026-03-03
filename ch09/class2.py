# class2.py

class Cexm:
    # 멤버 변수 / 멤버 함수
    def fsam(self):
        print("멤버 함수(메소드)")

    def fsbm(self, pa):
        self.x = pa
        print("인스턴트 멤버 변수 x: ", self.x)

ca = Cexm()
ca.fsam()
ca.fsbm(1)

cb = Cexm()
cb.fsam()
cb.fsbm(2)


# 클래스: 가방
# 객체 : 숄더백, 캐리어, 핸드백, 클러치백
# 속성:  재질, 색, 무게, 용량, 가격, 수납개수
# 기능 : 넣기, 꺼내기, 꾸미기

class Bag:
    # 멤버 변수
    color = "검정색"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.data = []

    # 메서드 = 멤버함수
    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

back_pack = Bag("백팩", "검정색")
print(back_pack.color)
back_pack.add("휴대폰")
print(back_pack.data)

back_pack.addtwice("연필")
print(back_pack.data)

print(back_pack.name)


handbag = Bag("핸드백", "노랑색")
print(handbag.color)
handbag.add("지갑")
handbag.add("책")
print(handbag.data)



class Cadd:
    def fadd(self, a, b):
        self.x = a
        self.y = b
        self.hap = self.x + self.y
obj = Cadd()
obj.fadd(10,20)
print(f"x:{obj.x}")
print(f"y:{obj.y}")
print(f"합:{obj.hap}")


class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + '살 ' + self.name + '입니다.')

man1 = Human(22, "kim")
man1.intro()
man2 = Human(33, "lee")
man2.intro()









