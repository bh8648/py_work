# radio.py

from tkinter import Tk, Button, Radiobutton, IntVar

obj_root = Tk() # 부모 윈도우(위젯)
obj_root.geometry("400x300")

lunch = {0:'A런치', 1:'B런치', 2:'C런치'}

radio_value = IntVar() # 정수형 변수 생성
radio_value.set(-1) # set : 정수를 담을 수 있는 공간에 데이터를 직접적으로 삽입 가능 // 지금은 -1을 담아서 아무것도 선택 안함

# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터 지정하는 인수
obj_rb1 = Radiobutton(obj_root, text=lunch[0], variable=radio_value, value=0)
obj_rb2 = Radiobutton(obj_root, text=lunch[1], variable=radio_value, value=1)
obj_rb3 = Radiobutton(obj_root, text=lunch[2], variable=radio_value, value=2)
obj_rb1.pack()
obj_rb2.pack()
obj_rb3.pack()


def buy():
    # 주문을 누르면 buy가 실행되는데 buy에서는 radio_value에 있는 키 값을 가져와서 출력
    value = radio_value.get() # 설정된 데이터를 가져와 확인 가능
    print(lunch[value])

obtn = Button(obj_root, text="주문", command=buy)
obtn.pack()


obj_root.mainloop()



# # 대략적인 IntVar 클래스의 get(), set() 구현

# class IntVar():
#     def __init__(self):
#         self.value = 0    
#     def set(self,value):
#         self.value = value
#     def get():
#         return self.value



