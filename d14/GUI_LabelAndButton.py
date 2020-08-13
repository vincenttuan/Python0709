import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
win.geometry("300x300")
label = tkinter.Label(win, text="Hello")
label.pack()
button1 = tkinter.Button(win, text="OK")
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(win, text="Exit")
button2.pack(side=tkinter.RIGHT)

win.mainloop()