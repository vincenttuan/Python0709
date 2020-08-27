import tkinter
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

def add():
    sid = int(entry_sid.get())
    h = float(entry_h.get())
    w = float(entry_w.get())
    cursor.execute('INSERT INTO bmi(h, w, sid) VALUES(%f, %f, %d)' % (h, w, sid))
    conn.commit()
    query()

def delete():
    id = int(entry_sid.get())
    cursor.execute('DELETE FROM bmi WHERE id = %d' % (id))
    conn.commit()
    query()

def query():
    # 清空 tree 的資料
    for i in tree.get_children():
        tree.delete(i)

    sql = 'SELECT b.id, b.h, b.w, ROUND(b.w / ((b.h / 100)*(b.h / 100)), 2) AS bmi, s.name, s.id ' \
          'FROM student as s, bmi as b ' \
          'WHERE s.id = b.sid ' \
          'ORDER BY bmi DESC'

    cursor.execute(sql)
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

win = tkinter.Tk()
win.title('BMI')
my_frame = ttk.Frame(win)
my_frame.pack()
my_frame2 = ttk.Frame(win)
my_frame2.pack()
entry_sid = tkinter.Entry(my_frame, justify=tkinter.CENTER)
entry_h = tkinter.Entry(my_frame, justify=tkinter.CENTER)
entry_w = tkinter.Entry(my_frame, justify=tkinter.CENTER)
entry_sid.pack(side=tkinter.LEFT)
entry_h.pack(side=tkinter.LEFT)
entry_w.pack(side=tkinter.LEFT)

addButton = tkinter.Button(my_frame2, text='新增', command=add)
delButton = tkinter.Button(my_frame2, text='刪除', command=delete)
queryButton = tkinter.Button(my_frame2, text='查詢', command=query)
addButton.pack(side=tkinter.LEFT)
delButton.pack(side=tkinter.LEFT)
queryButton.pack(side=tkinter.LEFT)

tree = ttk.Treeview(win, columns=['1', '2', '3', '4', '5', '6'], show='headings') # 表格
tree.heading('1', text='序號')
tree.heading('2', text='身高')
tree.heading('3', text='體重')
tree.heading('4', text='BMI')
tree.heading('5', text='姓名')
tree.heading('6', text='sid')

tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')
tree.column('3', width=100, anchor='center')
tree.column('4', width=100, anchor='center')
tree.column('5', width=100, anchor='center')
tree.column('6', width=100, anchor='center')

query()

tree.pack()
win.mainloop()