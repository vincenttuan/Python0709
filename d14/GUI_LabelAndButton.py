import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
win.geometry("300x300")
label = tkinter.Label(win, text="Hello")
label.pack()

win.mainloop()