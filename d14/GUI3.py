import tkinter

def add():
    n = ans.get()
    n = n + 1
    ans.set(n)

win = tkinter.Tk()
win.title("My Add")
win.geometry("200x200")

ans = tkinter.IntVar()
ans.set(0)
label = tkinter.Label(win, textvariable=ans)
label.config(font=("Arial", 30))
label.pack()

addButton = tkinter.Button(win, text="Add", command=add)
addButton.config(font=("Arial", 30))
addButton.pack()

win.mainloop()