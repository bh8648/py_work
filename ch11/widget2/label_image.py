# label_image.py

from tkinter import Tk, Label, Button, PhotoImage

oroot=Tk()
oroot.geometry('400x300')

img1= PhotoImage(file=r'ch11\widget2\\apple.png') # png파일만 사용가능
img_label = Label(oroot, image=img1)
img_label.place(x=-500,y=-100) # pack으로 해도 됨.

obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")
obutton1.place(x=10, y=60)
obutton2.place(x=140, y=60)
obutton3.place(x=80, y=10)


oroot.mainloop()
