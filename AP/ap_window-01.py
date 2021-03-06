


import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog
import json
import re
from itertools import groupby



root = tk.Tk()
# root.withdraw()

# print(file_path)

fe_store = []
join_store = []
store_count = []
last_count = -1

# 打开json文件并把存储在一个list中
def open_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for part in data:
            split_data = re.findall(r'.{20}', part)
            for i in split_data:
                fe_store.append(i)

# 显示笔的坐标数据和count
def show_json_and_count():
    global last_count
    for i in fe_store:
        cm = 0

        if i.startswith('FC'):
            fc_num = int(i[-2:], base=16)

            if last_count != -1:
                if fc_num < last_count:
                    cm = fc_num + 247
                else:
                    cm = fc_num
                if cm - last_count != 1:
                    print('red')
            last_count = fc_num

            print('{:<40}, count = {}'.format(i, fc_num))

            i_fc_num = i + ' '*40 + 'count = ' + str(fc_num)
            listbox.insert(tk.END,  i_fc_num)
            store_count.append(fc_num)
        elif i.startswith('FE'):
            if i[3] == '1':
                join_store.append(i)
            if i[3] == '2':
                join_store.append(i)
                a = join_store[0] + join_store[1]   # 拼接两个FE
                fe_num = int(i[-10:-8], base=16)

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

                print('{:<40}, count = {}'.format(a, fe_num))
                i_fe_num = i + ' ' * 40 + 'count =' + str(fe_num)
                listbox.insert(tk.END, i_fe_num)
                join_store.clear()

# 显示连续数字范围
def continue_num_range():
    fun = lambda x : x[1] - x[0]
    for k, g in groupby(enumerate(store_count), fun):
        l1 = [j for i, j in g]
        if len(l1) > 1:
            scope = str(min(l1)) + '-' + str(max(l1))
        else:
            scope = l1[0]
        print('连续数字范围：{}'.format(scope))

def import_json_btn():
    listbox.delete(0, tk.END)
    file_path = filedialog.askopenfilename()
    open_json(file_path)
    show_json_and_count()
    continue_num_range()

    # 清空list

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