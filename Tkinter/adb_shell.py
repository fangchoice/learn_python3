
"""
  将D盘下client_server.txt烧录到 硬件设备中，
  烧录成功则显示OK，反之则显示Fail。
"""


import os 
import tkinter
from tkinter import *

top = tkinter.Tk()
top.geometry('200x200')

# cmd
def run_cmd():
	adb = 'adb devices'
	adb_push = 'adb push d:\\client_server.txt /etc'
	d = os.system(adb)
	# print(d)
	push = os.system(adb_push)
	# print(push)
	if push == 0:
		text.delete(1.0, END)
		text.insert("insert", "OK\n", 'tag')
		
	else:
		text.delete(1.0, END)
		text.insert("insert", "Fail\n", 'tag_1')
		
# 控件
scroll = Scrollbar()
text = Text(top, width=20, height=5)

# 通过tag这个属性改变显示的文字的颜色
text.tag_add('tag', 1.0)
text.tag_config('tag', foreground='green')
text.tag_add('tag_1', 1.0)
text.tag_config('tag_1', foreground='red')

btn = tkinter.Button(top, text="烧录IP", command=run_cmd)

btn.pack()

text.pack(side=LEFT, fill=Y)
# 显示滚动条位置，放在右侧  填充满Y轴
scroll.pack(side=RIGHT, fill=Y)
# 绑定滚动条和文本框
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
top.mainloop()
