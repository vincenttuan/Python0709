# 現在時間
import tkinter
import datetime
import time

def play():
    dt = datetime.datetime.today()
    ans.set(dt)


win = tkinter.Tk()
win.title("My Add")
win.geometry("500x100")

ans = tkinter.StringVar()
ans.set("")
label = tkinter.Label(win, textvariable=ans)
label.config(font=("Arial", 20))
label.pack()

addButton = tkinter.Button(win, text="Start", command=play)
addButton.config(font=("Arial", 20))
addButton.pack()

win.mainloop()