import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox


window = tk.Tk()
window.title('登录界面')       # 设置窗口的标题
window.geometry('500x400')     # 设置窗口的大小

# 画布放在window的顶部
canvas = tk.Canvas(window, height=200, width=500)
canvas.pack(side='top')

image_file = ImageTk.PhotoImage(file='./pic/login.png')
# 以图片中心定位到 (250, 100) 的位置上
image = canvas.create_image(250, 100, anchor='center', image=image_file)

# 输入框的提示语
tk.Label(window, text="用户名:").place(x=75, y=250, anchor='nw')
tk.Label(window, text="密码  :").place(x=75, y=280, anchor='nw')

# 两个输入框
usr_name_var = tk.StringVar()
password_var = tk.StringVar()
tk.Entry(window, textvariable=usr_name_var).place(x=150, y=250, anchor='nw')
tk.Entry(window, textvariable=password_var, show='*').place(x=150, y=280, anchor='nw')

def login():
    user_name = usr_name_var.get()
    messagebox.showinfo(title='登录成功', message="欢迎你， {name}".format(name=user_name))

# 登录按钮
tk.Button(window, text='登录', command=login).place(x=280, y=350)

window.mainloop()