


import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog
import json
import os
import re
from itertools import groupby



root = tk.Tk()
# root.withdraw()

# print(file_path)

fe_store = []
join_store = []
store_count = []
last_count = -1
flag = 0

# 打开json文件并把存储在一个list中
def open_json(file_path):
    with open(file_path, 'r') as f:
        # data = json.load(f)
        data = f.read()
        data = data.replace(',','')
        # print('data length: ',len(data))
        # print(data)

        split_data = re.findall(r'.{20}', data)
        # print(split_data)
        for i in split_data:
        	# print(i)
        	fe_store.append(i)



# 显示笔的坐标数据和count,压力值
def show_json_and_count():
    global last_count
    for i in fe_store:
        cm = 0
        # print(i)
        if i.startswith('fc'):
            fc_num = int(i[-2:], base=16)

            force_value = int(i[-4:-2], base=16)

            if last_count != -1:
                if fc_num < last_count:
                    cm = fc_num + 247

                # elif force_value == 0:
                # 	fc_num += 1
                else:
                    cm = fc_num
                if cm - last_count != 1:
                    print('red')
            last_count = fc_num

            print('{:<40}, count = {:<4}, force_value = {}'.format(i, fc_num, force_value))
            # print(i)

            i_fc_num = i + ' '*40 + 'count = ' + str(fc_num) + '      force value =' + str(force_value)
            listbox.insert(tk.END,  i_fc_num)
            store_count.append(fc_num)
        elif i.startswith('fe'):
            if i[3] == '1':
                join_store.append(i)
            if i[3] == '2':
                join_store.append(i)
                a = join_store[0] + join_store[1]   # 拼接两个FE
                fe_num = int(i[-10:-8], base=16)

                fe_force_value = int(i[-12:-10], base=16)

                store_count.append(fe_num)
                if last_count != -1:
                    if fe_num < last_count:
                        cm = fe_num + 247
                    else:
                        cm = fe_num
                    if cm - last_count != 1:
                        print('red')
                        listbox.insert(tk.END, label)

                last_count = fe_num

                print('{:<40}, count = {:<4}, force_value = {}'.format(a, fe_num, fe_force_value))
                # print(a)

                i_fe_num = i + ' ' * 40 + 'count =' + str(fe_num) + '      force value =' + str(fe_force_value)
                listbox.insert(tk.END, i_fe_num)
                join_store.clear()

# 显示连续数字范围
def continue_num_range():
	
    fun = lambda x : x[1] - x[0]
    discard_num = 0
    # discard_count = 0
    for k, g in groupby(enumerate(store_count), fun):
        l1 = [j for i, j in g]
        if len(l1) > 1:
            scope = str(min(l1)) + '-' + str(max(l1))
            if min(l1) > 0 or max(l1) < 246:
            	discard_num += 1
            	# discard_count += max(l1) - min(l1)
        else:
            scope = l1[0]
        print('连续数字范围：{}'.format(scope))
    print('-'*70)
    # 排除第一个元素不是从零开始和最一个元素不是246的情况
    if discard_num - 2 >=0:
    	print("丢数据的次数：{}".format( discard_num - 2 ))
    else:
    	print("丢数据的次数：{}".format(0))
    print('-'*70)
    # print("丢数据的总点数：{}".format(discard_count))
    # print('-'*70)

def import_json_btn():
    listbox.delete(0, tk.END)
    file_path = filedialog.askopenfilename()
    open_json(file_path)
    show_json_and_count()
    continue_num_range()

    # 清空list.

    last_count = -1
    fe_store.clear()
    store_count.clear()
    join_store.clear()

# 控件
label = tk.Label(root, text='选择一个Json文件', width=20, height=1)
button = tk.Button(root, text='ImportAndShow', command=import_json_btn,)
listbox = tk.Listbox(root, width=110, height=30)
scrollbar = ttk.Scrollbar(root, orient='vertical', command=listbox.yview)

# 表格布局
label.grid(row=0, column=0, padx=10, pady=10)
button.grid(row=0, column=1, padx=10, pady=10)
listbox.grid(row=1, column=0, columnspan=5, rowspan=5)
scrollbar.grid(row=1, column=5, rowspan=5, sticky='ns')


root.geometry('800x600')
root.minsize(800, 600)
root.maxsize(800, 600)
root.mainloop()

