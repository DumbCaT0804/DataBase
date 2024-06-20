import tkinter as tk # 导入tkinter 模块

root = tk.Tk() # 创建Tk的类实例 -> 生成应用窗口 也就是说root 就是 window窗口

# add a label widget 添加组件
message = tk.Label(root, text="hello world")
message.pack() # the widget 可视化

# 改变窗口标题 window.title(new_title)
root.title('DataBase')
title = root.title()    #获取当前窗口标题
print(title)

# 改变窗口大小和位置 window.geometry(new_geometry) width * height +- x +- y
window_width = 1440
window_height = 960

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 居中窗口
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# 让窗口大小不可改变
root.resizable(False, False)

# 当窗口大小可改变时， 最大和最小窗口范围
# window.minsize(min_width, min_height)
# window.maxsize(max_height, max_height) window指的是你创建的窗口类的实例

# transparency 透明度
root.attributes('-alpha', 0.0)

# 窗口堆叠顺序
root.attributes('-topmost', 1)

root.mainloop() 