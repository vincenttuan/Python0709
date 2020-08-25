import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msg


# ===================================backspace=====================================


def reset():
    global isEqual
    global isPoint
    isEqual = False
    isPoint = False


def clear():
    ans.set("")
    reset()


def back():
    a = ans.get()
    if a[len(a) - 1] == ' ':
        a = a[:len(a) - 3]
    else:
        pos = a[len(a) - 1]
        print(pos)
        if pos == '.':
            global isPoint
            isPoint = False
        a = a[:len(a) - 1]
    ans.set(a)


# ===================================number=====================================


def checkEqual():
    global isEqual
    if isEqual:
        isEqual = False
        ans.set("")


def checkZero():
    if len(ans.get()) == 0:
        return True
    if not ans.get().__contains__(" "):
        if ans.get()[0] == '0':
            return "replace"
        return True
    symbolList = ['+', '-', '*', '/']
    index = []
    for symbol in symbolList:
        index.append(ans.get().rfind(symbol))
    i = max(index)
    a = ans.get()[i + 1:]

    def checkagain(a):
        if len(a) == 0:
            return True
        if a[0] == '0':
            return "replace"
        return True

    a = a.replace(' ', '')
    return checkagain(a)


def m0():
    checkEqual()
    if len(ans.get()) == 0:
        ans.set(ans.get() + "0")
        return
    if not ans.get().__contains__(" "):
        if ans.get()[0] != '0' or isPoint:
            ans.set(ans.get() + "0")
            return
    symbolList = ['+', '-', '*', '/']
    index = []
    for symbol in symbolList:
        index.append(ans.get().rfind(symbol))
    i = max(index)
    a = ans.get()[i + 1:]

    def m0_1(a):
        if len(a) == 1:
            a = a + "0"
            return a
        a.replace(' ', '')
        if a[1] != '0' or isPoint:
            a = a + "0"
            return a

    if m0_1(a) is None:
        return
    ans.set(ans.get()[:i + 1] + m0_1(a))


def m1():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "1")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "1")
        return
    ans.set(ans.get() + "1")


def m2():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "2")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "2")
        return
    ans.set(ans.get() + "1")


def m3():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "3")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "3")
        return
    ans.set(ans.get() + "3")


def m4():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "4")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "4")
        return
    ans.set(ans.get() + "4")


def m5():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "5")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "5")
        return
    ans.set(ans.get() + "5")


def m6():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "6")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "6")
        return
    ans.set(ans.get() + "6")


def m7():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "7")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "7")
        return
    ans.set(ans.get() + "7")


def m8():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "8")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "8")
        return
    ans.set(ans.get() + "8")


def m9():
    checkEqual()
    i = checkZero()
    if i is True:
        ans.set(ans.get() + "9")
        return
    elif i == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 1] + "9")
        return
    ans.set(ans.get() + "9")


# ===================================symbol=====================================


def checkSymbol():
    a = ans.get()
    if a == '':
        return None
    elif a[len(a) - 1] == '.':
        ans.set(a + "0")
        return True
    elif not a[len(a) - 2].isdigit() and a[len(a) - 2] != '.':
        return "replace"
    else:
        return True


def checkSymbolEqual():
    global isEqual
    if isEqual:
        isEqual = False


def add():
    global isPoint
    symbol = checkSymbol()
    if symbol is None:
        ans.set("")
    elif symbol == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 3] + " + ")
    else:
        ans.set(ans.get() + " + ")
    checkSymbolEqual()
    isPoint = False


def minus():
    global isPoint
    symbol = checkSymbol()
    if symbol is None:
        ans.set("")
    elif symbol == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 3] + " - ")
    else:
        ans.set(ans.get() + " - ")
    checkSymbolEqual()
    isPoint = False


def time():
    global isPoint
    symbol = checkSymbol()
    if symbol is None:
        ans.set("")
    elif symbol == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 3] + " * ")
    else:
        ans.set(ans.get() + " * ")
    checkSymbolEqual()
    isPoint = False


def div():
    global isPoint
    symbol = checkSymbol()
    if symbol is None:
        ans.set("")
    elif symbol == 'replace':
        ans.set(ans.get()[:len(ans.get()) - 3] + " / ")
    else:
        ans.set(ans.get() + " / ")
    checkSymbolEqual()
    isPoint = False


def equal():
    global isEqual
    global isPoint
    a = ans.get()
    if a == '':
        ans.set("0")
        isEqual = True
    elif not a[len(a) - 1].isdigit():
        msg.showerror('錯誤', '輸入函式錯誤')
    elif not a.isdigit():
        global records
        a = eval(ans.get().replace(' ', ''))
        if a is float:
            a = "%.2f" % a
            checkExist(ans.get() + " = " + a)
            ans.set(a)
        else:
            checkExist(ans.get() + " = " + str(a))
            ans.set(a)
        isEqual = True
        isPoint = False


def point():
    a = ans.get()
    global isPoint
    if not isPoint:
        if ans.get() == '' or not a[len(a) - 1].isdigit():
            ans.set(ans.get() + "0.")
        else:
            ans.set(ans.get() + ".")
        isPoint = True


# ===================================function====================================


def checkExist(string):
    global records
    if records.__contains__(string):
        return
    records.append(string)
    record_combobox['value'] = records


def show():
    global isShow
    if isShow:
        record_combobox.grid_forget()
        isShow = False
    else:
        record_combobox.grid(row=0, column=4, rowspan=5, sticky="EWN")
        isShow = True


def fill(event):
    string = record_combobox.get()
    index = str(string).index('=')
    string = string[:index - 1]
    ans.set(string)


if __name__ == '__main__':
    win = tk.Tk()

    win.title("計算機")
    win.geometry("500x400")
    win.config(bg='#D3D3D3')

    f = ("Arial", 20)

    # Button
    btn_clear = tk.Button(win, text='C', font=f, command=clear, bg='gray', fg='white')
    btn_back = tk.Button(win, text='<-', font=f, command=back, bg='gray', fg='white')
    btn_div = tk.Button(win, text='/', font=f, command=div, bg='gray', fg='white')
    btn_7 = tk.Button(win, text='7', font=f, command=m7, bg='black', fg='white')
    btn_8 = tk.Button(win, text='8', font=f, command=m8, bg='black', fg='white')
    btn_9 = tk.Button(win, text='9', font=f, command=m9, bg='black', fg='white')
    btn_time = tk.Button(win, text='*', font=f, command=time, bg='gray', fg='white')
    btn_4 = tk.Button(win, text='4', font=f, command=m4, bg='black', fg='white')
    btn_5 = tk.Button(win, text='5', font=f, command=m5, bg='black', fg='white')
    btn_6 = tk.Button(win, text='6', font=f, command=m6, bg='black', fg='white')
    btn_minus = tk.Button(win, text='-', font=f, command=minus, bg='gray', fg='white')
    btn_1 = tk.Button(win, text='1', font=f, command=m1, bg='black', fg='white')
    btn_2 = tk.Button(win, text='2', font=f, command=m2, bg='black', fg='white')
    btn_3 = tk.Button(win, text='3', font=f, command=m3, bg='black', fg='white')
    btn_add = tk.Button(win, text='+', font=f, command=add, bg='gray', fg='white')
    btn_0 = tk.Button(win, text='0', font=f, command=m0, bg='black', fg='white')
    btn_point = tk.Button(win, text='.', font=f, command=point, bg='black', fg='white')
    btn_equ = tk.Button(win, text='=', font=f, command=equal, bg='gray', fg='white')
    btn_record = tk.Button(win, text='紀錄', font=("Arial", 15), command=show, bg='gray', fg='white')

    # Label
    ans = tk.StringVar()
    label_ans = ttk.Label(win, textvariable=ans, font=("Arial", 22), anchor=tk.E)

    # Combobox
    records = []
    record_combobox = ttk.Combobox(win, value=records, state='readonly', height=5)
    record_combobox.bind("<<ComboboxSelected>>", fill)

    # put in

    win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    win.columnconfigure((0, 1, 2, 3), weight=5)

    col_count, row_count = win.grid_size()

    label_ans.grid(row=0, column=1, columnspan=3, sticky="EWNS")
    btn_clear.grid(row=1, column=0, columnspan=2, sticky="EWNS", padx=1, pady=1)
    btn_back.grid(row=1, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_div.grid(row=1, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_7.grid(row=2, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_8.grid(row=2, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_9.grid(row=2, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_time.grid(row=2, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_4.grid(row=3, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_5.grid(row=3, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_6.grid(row=3, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_minus.grid(row=3, column=3, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_1.grid(row=4, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_2.grid(row=4, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_3.grid(row=4, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_add.grid(row=4, column=3, rowspan=2, sticky="EWNS", padx=1, pady=1)
    btn_0.grid(row=5, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_point.grid(row=5, column=1, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_equ.grid(row=5, column=2, columnspan=1, sticky="EWNS", padx=1, pady=1)
    btn_record.grid(row=0, column=0, columnspan=1, sticky="EWNS", padx=1, pady=1)
    record_combobox.grid(row=0, column=4, rowspan=5, sticky="EWN")

    record_combobox.grid_forget()

    # config
    isShow = False
    isEqual = False
    isPoint = False

    win.mainloop()