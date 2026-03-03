# Human.py

# Super Class(부모)
class Human:
    # 멤버변수(속성)
    eyes = 2
    nose = 1
    mouth = 1

    # 멤버함수=메서드 (기능/동작)

    # 생성자 함수
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def talk(self):
        print("말하다")
    def eat(self):
        print('먹다')
    def sleep(self):
        print("자다")
    def introduce(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")


# Sub Class(자식)
class Student(Human):
    
    def __init__(self, name, age, studentNum):
        super().__init__(name, age)
        self.studentNum = studentNum

    def introduce(self):
        super().introduce()
        print("human에서는 이름이랑 나이 말하고 여기서는 애옹~")
    
    def study(self):
        print("공부하다")



lee = Human("Lee", 33)
lee.introduce()
lee.eat()
lee.sleep()
print(lee.eyes)
print("========================")
kim = Student("kim", 44, 20260226)
kim.introduce()
kim.eat()
kim.sleep()
kim.study()
print(kim.nose)


