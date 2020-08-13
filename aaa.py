import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, win):
        win.geometry("300x200")
        ttk.Frame.__init__(self, win)
        self.pack()

win = tk.Tk()
app = Application(win)
win.mainloop()