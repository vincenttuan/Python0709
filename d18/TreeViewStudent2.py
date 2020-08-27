import tkinter
import sqlite3
from tkinter import ttk

win = tkinter.Tk()

entry = tkinter.Entry(win, justify=tkinter.CENTER)
entry.pack()

addButton = tkinter.Button(win, text='新增')
addButton.pack()

queryButton = tkinter.Button(win, text='查詢')
queryButton.pack()

tree = ttk.Treeview(win, columns=['1', '2'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='姓名')

tree.column('1', width=200, anchor='center')
tree.column('2', width=200, anchor='center')

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute('select id, name from student')
for row in cursor.fetchall():
    tree.insert('', 'end', values=row)

tree.pack()
win.mainloop()