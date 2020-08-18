import tkinter
from firebase import firebase
firebase = firebase.FirebaseApplication('https://iotfb-fc0b9.firebaseio.com/', None)

def openTheDoor():
    result = firebase.patch('/myhouse', {'open': 1})

def closeTheDoor():
    result = firebase.patch('/myhouse', {'open': 0})

win = tkinter.Tk()
win.title("Door Open")
win.geometry("300x100")

openButton = tkinter.Button(win, text="Open", command=openTheDoor)
openButton.config(font=("Arial", 20))
openButton.pack(side=tkinter.LEFT)

closeButton = tkinter.Button(win, text="Close", command=closeTheDoor)
closeButton.config(font=("Arial", 20))
closeButton.pack(side=tkinter.RIGHT)

win.mainloop()