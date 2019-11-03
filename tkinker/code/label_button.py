import tkinter as tk

window = tk.Tk()
# 窗口的名字
window.title('my window')
# 窗口的小尺寸
window.geometry('500x400')


# 设置字符串的变量,相当于一个存储器
var = tk.StringVar()


# 这里是窗口的内容
# 所有的object 都是要大写开头的
# label 的的参数 窗口的名字， 窗口上文字的类型及内容， bg 背景颜色 font 字体大小
l = tk.Label(window,
             #  text='OMG! this is TK!',    # 标签的文字
             textvariable=var,  # # 使用 textvariable 替换 text, 因为这个可以变化
             bg='green',     # 背景颜色
             font=('Arial', 12),     # 字体和字体大小
             width=15, height=2  # 标签长宽
             )
l.pack()    # 固定窗口位置
# l.place()   # 放到一个准确的点


# 添加 hit_me 命令函数
on_hit = False


def hit_me():
    global on_hit  # 定义之后，别忘了在函数中获取
    if on_hit == False:
        on_hit = True
        # 设置var的内容
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")


# 按钮 tk.button
b = tk.Button(window,
              text='hit me',      # 显示在按钮上的文字
              width=15, height=2,
              command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置 这个放在谁下面，button的就在谁下面


# while 循环的作用，mainloop
window.mainloop()
