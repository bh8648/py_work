# checkbutton.py
from tkinter import Tk, Button, BooleanVar, Checkbutton

oroot = Tk()
oroot.geometry("400x300")

check_value = {}
coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노", 3:"에스프레소"}

for i in range(len(coffee)):
    check_value[i] = BooleanVar() # Boolean 값 저장
    ocheckbutton = Checkbutton(oroot, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack()

# check_value[0].set(True)

# print(check_value[0].get())
def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(coffee[i])
    print(end="\n\n\n")

    
obtn = Button(oroot, text="주문", command=buy)
obtn.pack()

obtn.mainloop()
