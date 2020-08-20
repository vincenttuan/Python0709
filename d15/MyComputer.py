import tkinter
import tkinter.ttk as ttk

def b1():
    var.set(var.get() + "1")
def b2():
    var.set(var.get() + "2")
def b3():
    var.set(var.get() + "3")
def b4():
    var.set(var.get() + "4")
def b5():
    var.set(var.get() + "5")
def b6():
    var.set(var.get() + "6")
def b7():
    var.set(var.get() + "7")
def b8():
    var.set(var.get() + "8")
def b9():
    var.set(var.get() + "9")
def b0():
    var.set(var.get() + "0")
def bdot():
    var.set(var.get() + ".")
    pass
def bsubmit():
    var.set("%.2f" % eval(var.get()))
    pass
def badd():
    var.set(var.get() + "+")
    pass
def bsub():
    var.set(var.get() + "-")
    pass
def bmul():
    var.set(var.get() + "*")
    pass
def bdiv():
    var.set(var.get() + "/")
    pass
def bback():
    s = var.get()
    var.set(s[:len(s)-1])
    pass
def bclear():
    var.set("")
    pass

win = tkinter.Tk()
win.title('我的計算機')

s = ttk.Style()
s.configure('My.TButton', font=('Arial', 20))

var = tkinter.StringVar()
var.set("")

my_label = ttk.Label(win, textvariable=var, font=('Arial', 20), anchor=tkinter.E)
btn1 = ttk.Button(win, text='1', style='My.TButton', command=b1)
btn2 = ttk.Button(win, text='2', style='My.TButton', command=b2)
btn3 = ttk.Button(win, text='3', style='My.TButton', command=b3)
btn4 = ttk.Button(win, text='4', style='My.TButton', command=b4)
btn5 = ttk.Button(win, text='5', style='My.TButton', command=b5)
btn6 = ttk.Button(win, text='6', style='My.TButton', command=b6)
btn7 = ttk.Button(win, text='7', style='My.TButton', command=b7)
btn8 = ttk.Button(win, text='8', style='My.TButton', command=b8)
btn9 = ttk.Button(win, text='9', style='My.TButton', command=b9)
btn0 = ttk.Button(win, text='0', style='My.TButton', command=b0)
btndot = ttk.Button(win, text='.', style='My.TButton', command=bdot)
btnsubmit = ttk.Button(win, text='=', style='My.TButton', command=bsubmit)
btnadd = ttk.Button(win, text='+', style='My.TButton', command=badd)
btnsub = ttk.Button(win, text='-', style='My.TButton', command=bsub)
btnmul = ttk.Button(win, text='*', style='My.TButton', command=bmul)
btndiv = ttk.Button(win, text='/', style='My.TButton', command=bdiv)
btnback = ttk.Button(win, text='<-', style='My.TButton', command=bback)
btnclear = ttk.Button(win, text='C', style='My.TButton', command=bclear)

win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  # row 同步放大縮小
win.columnconfigure((0, 1, 2, 3), weight=1)  # column 同步放大縮小

my_label.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='EWNS', padx=(20))
btnclear.grid(row=1, column=0, columnspan=2, rowspan=1, sticky='EWNS')
btnback.grid(row=1, column=2, columnspan=1, rowspan=1, sticky='EWNS')
btndiv.grid(row=1, column=3, columnspan=1, rowspan=1, sticky='EWNS')

btn7.grid(row=2, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btn8.grid(row=2, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btn9.grid(row=2, column=2, columnspan=1, rowspan=1, sticky='EWNS')
btnmul.grid(row=2, column=3, columnspan=1, rowspan=1, sticky='EWNS')

btn4.grid(row=3, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btn5.grid(row=3, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btn6.grid(row=3, column=2, columnspan=1, rowspan=1, sticky='EWNS')
btnsub.grid(row=3, column=3, columnspan=1, rowspan=1, sticky='EWNS')

btn1.grid(row=4, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btn2.grid(row=4, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btn3.grid(row=4, column=2, columnspan=1, rowspan=1, sticky='EWNS')
btnadd.grid(row=4, column=3, columnspan=1, rowspan=2, sticky='EWNS')

btn0.grid(row=5, column=0, columnspan=1, rowspan=1, sticky='EWNS')
btndot.grid(row=5, column=1, columnspan=1, rowspan=1, sticky='EWNS')
btnsubmit.grid(row=5, column=2, columnspan=1, rowspan=1, sticky='EWNS')


win.mainloop()

