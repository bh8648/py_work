import tkinter as tk
from tkinter import messagebox

class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍕 델리 피자 주문 시스템")
        self.root.geometry("400x500")

        # 피자 메뉴 및 가격 (조각당)
        self.menu = {
            "페퍼로니 피자": 4500,
            "치즈 피자": 4000,
            "포테이토 피자": 5000,
            "불고기 피자": 5500
        }

        # 변수 설정
        self.selected_pizza = tk.StringVar(value="페퍼로니 피자")
        self.quantity = tk.IntVar(value=1)

        self.setup_ui()

    def setup_ui(self):
        # 제목 레이블
        title_label = tk.Label(self.root, text="원하는 조각 피자를 선택하세요", font=("Arial", 16, "bold"), pady=20)
        title_label.pack()

        # 메뉴 선택 (라디오 버튼)
        menu_frame = tk.LabelFrame(self.root, text="메뉴판", padx=20, pady=10)
        menu_frame.pack(pady=10, fill="x", padx=30)

        for pizza, price in self.menu.items():
            rb = tk.Radiobutton(menu_frame, text=f"{pizza} ({price}원)", 
                                variable=self.selected_pizza, value=pizza, font=("Arial", 11))
            rb.pack(anchor="w")

        # 수량 입력
        qty_frame = tk.Frame(self.root, pady=20)
        qty_frame.pack()
        
        tk.Label(qty_frame, text="수량: ", font=("Arial", 12)).grid(row=0, column=0)
        qty_spinbox = tk.Spinbox(qty_frame, from_=1, to=20, textvariable=self.quantity, width=5, font=("Arial", 12))
        qty_spinbox.grid(row=0, column=1)
        tk.Label(qty_frame, text=" 조각", font=("Arial", 12)).grid(row=0, column=2)

        # 주문 버튼
        order_btn = tk.Button(self.root, text="주문하기", command=self.place_order, 
                              bg="#a52103", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        order_btn.pack(pady=20)

    def place_order(self):
        pizza = self.selected_pizza.get()
        count = self.quantity.get()
        price_per_slice = self.menu[pizza]
        total_price = price_per_slice * count

        # 주문 확인 메시지 박스
        order_summary = f"선택한 피자: {pizza}\n수량: {count}조각\n\n총 결제 금액: {total_price:,}원입니다."
        messagebox.showinfo("주문 완료", order_summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()