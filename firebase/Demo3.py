import tkinter

def openTheDoor():
    pass

def closeTheDoor():
    pass

win = tkinter.Tk()
win.title("Door Open")
win.geometry("300x100")

openButton = tkinter.Button(win, text="Open", command=openTheDoor)
openButton.config(font=("Arial", 20))
openButton.pack(side=tkinter.LEFT)

closeButton = tkinter.Button(win, text="Open", command=closeTheDoor)
closeButton.config(font=("Arial", 20))
closeButton.pack(side=tkinter.RIGHT)

win.mainloop()