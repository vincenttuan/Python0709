import tkinter
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

def add():
    name = entry.get()
    cursor.execute('INSERT INTO student(name) VALUES("%s")' % (name))
    conn.commit()
    query()

def query():
    # 清空 tree 的資料
    for i in tree.get_children():
        tree.delete(i)

    cursor.execute('select id, name from student')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

win = tkinter.Tk()

entry = tkinter.Entry(win, justify=tkinter.CENTER)
entry.pack()

addButton = tkinter.Button(win, text='新增', command=add)
addButton.pack()

queryButton = tkinter.Button(win, text='查詢', command=query)
queryButton.pack()

tree = ttk.Treeview(win, columns=['1', '2'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='姓名')

tree.column('1', width=200, anchor='center')
tree.column('2', width=200, anchor='center')

query()

tree.pack()
win.mainloop()