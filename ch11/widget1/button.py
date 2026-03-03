# button.py
from tkinter import *
from tkinter import Tk, Button
# 1. 위젯 생성
otk = Tk()
otk.geometry("400x300")
obtn1=Button(otk, text="PUSH1")
obtn2=Button(otk, text="PUSH2")
obtn3=Button(otk, text="PUSH3")


# 2. 위젯 배치
obtn1.pack()
obtn2.pack()
obtn3.pack()

otk.mainloop()


print("--------------------------------")















