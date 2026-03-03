# geometry_pack.py

from tkinter import Tk, Button
# 1. 위젯 생성
otk = Tk()
otk.geometry("400x300")
obtn1=Button(otk, text="PUSH1")
obtn2=Button(otk, text="PUSH2")
obtn3=Button(otk, text="PUSH3")


# 2. 위젯 배치 // pack과 grid는 함께 사용 불가. grid와 place도 불가

# obtn1.pack(side='left')
# obtn2.pack(side='right')
# obtn3.pack(side='top')


# obtn1.grid(row=3, column=0)
# obtn2.grid(row=1, column=1)
# obtn3.grid(row=0, column=4) # 상대적인 위치를 보는거라 4라고 해도 4의 위치가 아니라 같은 앞 열이 없으면 가장 앞으로 감(이산적 배치)


obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

otk.mainloop()
