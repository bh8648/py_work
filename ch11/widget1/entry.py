# entry.py

from tkinter import Tk, Label, Entry, StringVar
# 1. 위젯 생성
otk = Tk()
otk.geometry("400x300")

# StringVar: Tkinter에서 문자열 값을 저장/관리하는 특수 변수 객체
# 위젯의 값과 연결(textvariable)하면 값 변경이 위젯에 자동 반영
ostring = StringVar()

oentry = Entry(otk, textvariable=ostring) # textvariable : Entry에 입력하면 StringVar 값이 바뀌고, StringVar를 바꾸면 Entry 표시도 바뀜
olabel = Label(otk, textvariable=ostring) # # Label도 textvariable로 연결하면 StringVar 값이 Label 텍스트로 표시됨


# 2. 위젯 배치
oentry.pack()
olabel.pack()



otk.mainloop()



