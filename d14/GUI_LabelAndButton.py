import tkinter
from tkinter import messagebox

def hello():
    messagebox.showinfo('Hello', 'Python')

def cancel():
    win.quit()

win = tkinter.Tk()

win.title('我的小視窗')
win.geometry("300x300")
label = tkinter.Label(win, text="Hello")
label.config(font=("Arial", 40), bg="Red", fg="Yellow")
label.pack()

button1 = tkinter.Button(win, text="OK", command=hello)
button1.config(font=("Arial", 30))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Exit", command=cancel)
button2.config(font=("Arial", 30))
button2.pack(side=tkinter.RIGHT)

win.mainloop()