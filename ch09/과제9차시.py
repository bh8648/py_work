
# class Phone:
#     def __init__(self, 제조사, 출고년도, 색상):
#         print("휴대폰 생성")
#         self.제조사 = 제조사
#         self.출고년도 = 출고년도
#         self.색상 = 색상
    
#     def info(self):
#         print(self.제조사)
#         print(self.출고년도)
#         print(self.색상)

#     def setInfo(self, 제조사B, 출고년도B, 색상B):
#         self.제조사=제조사B
#         self.출고년도=출고년도B
#         self.색상=색상B

# my_phone = Phone("제조사A", '2026', '검은색')
# my_phone.info()
# my_phone.setInfo("제조사B", '2027', '하얀색')
# my_phone.info()

# print("======================================================")

# class Phone:
#     def __init__(self, number, color):
#         self.number = number
#         self.color = color
#     def showInfo(self):
#         print(f"전화번호: {self.number}")
#         print(f"색상: {self.color}")

# class SmartPhone(Phone):
#     def __init__(self, number, color, company):
#         super().__init__(number, color)
#         self.company = company
#     def showInfo(self):
#         super().showInfo()
#         print(f"회사: {self.company}")
        
# phone = Phone("010-1234-5678", "검정")
# phone.showInfo()
# apple = SmartPhone("010-1234-5678", "화이트", "애플")
# apple.showInfo()



# from tkinter import *

# oroot = Tk()
# oroot.geometry("400x300")
# oroot.title("조각 피자 주문 프로그램")
# label_pizza = Label(oroot, text="피자").pack()

# check_value = {}
# pizza_menu = {0:"치즈 피자 (3200원)", 1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
# pizza_price = {0: 3200, 1: 3500, 2: 3600}

# for i in range(len(pizza_menu)):
#     check_value[i] = BooleanVar()
#     obj_pizza_selection = Checkbutton(oroot, text=pizza_menu[i], variable=check_value[i])
#     obj_pizza_selection.pack(anchor="w")

# order_var = StringVar()
# order_var.set("주문내역:")
# total_var = StringVar()
# total_var.set("총 가격: 0원")

# def buy():
#     lines = ["주문내역:"]
#     total = 0
#     for i in check_value:
#         if check_value[i].get() == True:
#             lines.append("- " + pizza_menu[i])
#             total += pizza_price[i]

#     if len(lines) == 1:
#         lines.append("- (선택 없음)")

#     order_var.set("\n".join(lines))
#     total_var.set(f"총 가격: {total}원")

# obj_order = Button(oroot, text="주문", command=buy).pack()

# obj_order_finish = Label(oroot, textvariable=order_var).pack()
# obj_total_price = Label(oroot, textvariable=total_var).pack()

# oroot.mainloop()


numbers = [42, 17, 23, 56, 9, 34]
def list_max(num_list):
    max = num_list[0]
    for num in num_list:
        if max < num :
            max = num
    print(max)

list_max(numbers)


class Student:
    school = "hi"
    def __init__(self, name, grade):
        self.name = name
        self.grade=grade

s1 = Student("Aaa", 1)
print(Student.school)
print(s1.school)
print(s1.name)


from math import factorial
print(factorial(5))

print()
print()
print()
print()
print()
print()
print()

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return "Woof!"

Ani = Animal()
print(Ani.speak())
dog = Dog()
print(dog.speak())



import tkinter as tk
from tkinter import messagebox

def on_buton_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요", command=on_buton_click)
btn.pack(pady=20)

root.mainloop()

