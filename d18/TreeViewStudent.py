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

def delete():
    id = int(entry.get())
    cursor.execute('DELETE FROM student WHERE id = %d' % (id))
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
win.title('Student')
my_frame = ttk.Frame(win)
my_frame.pack()
entry = tkinter.Entry(my_frame, justify=tkinter.CENTER)
addButton = tkinter.Button(my_frame, text='新增', command=add)
delButton = tkinter.Button(my_frame, text='刪除', command=delete)
queryButton = tkinter.Button(my_frame, text='查詢', command=query)
entry.pack(side=tkinter.LEFT)
addButton.pack(side=tkinter.LEFT)
delButton.pack(side=tkinter.LEFT)
queryButton.pack(side=tkinter.LEFT)

tree = ttk.Treeview(win, columns=['1', '2'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='姓名')

tree.column('1', width=200, anchor='center')
tree.column('2', width=200, anchor='center')

query()

tree.pack()
win.mainloop()