# 現在時間
import tkinter
import datetime

def update():
    dt = datetime.datetime.today()
    ans.set(dt)

win = tkinter.Tk()
win.title("My Add")
win.geometry("500x100")

ans = tkinter.StringVar()
update()

label = tkinter.Label(win, textvariable=ans)
label.config(font=("Arial", 20))
label.pack()

addButton = tkinter.Button(win, text="Update", command=update)
addButton.config(font=("Arial", 20))
addButton.pack()

win.mainloop()