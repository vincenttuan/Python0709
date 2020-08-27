import tkinter
import sqlite3
from tkinter import ttk

win = tkinter.Tk()

tree = ttk.Treeview(win, columns=['1', '2'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='姓名')

tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('select id, name from student')
for row in cursor.fetchall():
    tree.insert('', 'end', values=row)

tree.grid()

tree.pack()
win.mainloop()