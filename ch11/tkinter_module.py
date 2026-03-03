# tkinter_module.py

# import tkinter

# # 1. 위젯 생성
# otk = tkinter.Tk()          # 부모 윈도우(위젯)
# obtn = tkinter.Button(text="click")     # 버튼 위젯

# # 2. 위젯 위치
# obtn.pack()

# # 3. 이벤트 바인딩
# # tkinter.Button(command=함수명)

# otk.mainloop()

# ==========================================================
# from tkinter import *

# otk = Tk()
# otk.geometry("1000x500+500+250")
# obtn=Button(otk, text="click")
# obtn.pack()

# otk.mainloop()

# ==========================================================
from tkinter import *

def hi():
    print("Hi there")

otk = Tk()
otk.geometry("400x300")
obtn=Button(otk, text="click", command=hi) # 버튼 오브젝트가 실행되면 거기에 맞추어 command 코드의 작업이 실행된다.

obtn.pack()

otk.mainloop()







