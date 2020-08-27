import tkinter
from tkinter import ttk

win = tkinter.Tk()

tree = ttk.Treeview(win, columns=['1', '2', '3'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='姓名')
tree.heading('3', text='年齡')

tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')
tree.column('3', width=100, anchor='center')

data1 = ['1', 'John', '男']
data2 = ['2', 'Mary', '女']
tree.insert('', 'end', values=data1)
tree.insert('', 'end', values=data2)
tree.grid()

tree.pack()
win.mainloop()