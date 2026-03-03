# option.py

import tkinter as tk

root = tk.Tk()
options_list = ['Option1', 'Option2', 'Option3']

selected_option = tk.StringVar()
selected_option.set(options_list[0])
option_menu = tk.OptionMenu(root, selected_option, *options_list)
option_menu.pack()


root.mainloop()
