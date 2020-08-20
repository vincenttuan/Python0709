import tkinter
import tkinter.ttk as ttk
win = tkinter.Tk()
win.title('Button 佈局')

s = ttk.Style()
s.configure('My.TButton', font=('Arial', 15))

btn1 = ttk.Button(win, text='1', style='My.TButton')
btn2 = ttk.Button(win, text='2', style='My.TButton')
btn3 = ttk.Button(win, text='3', style='My.TButton')
btn4 = ttk.Button(win, text='4', style='My.TButton')
btn5 = ttk.Button(win, text='5', style='My.TButton')
btn6 = ttk.Button(win, text='6', style='My.TButton')

win.rowconfigure((0, 1), weight=1)  # row 同步放大縮小
win.columnconfigure((0, 1, 2), weight=1)  # column 同步放大縮小

btn1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btn2.grid(row=0, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btn3.grid(row=0, column=2, columnspan=1, rowspan=1, sticky='EWNS')
btn4.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btn5.grid(row=1, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btn6.grid(row=1, column=2, columnspan=1, rowspan=1, sticky='EWNS')

win.mainloop()

