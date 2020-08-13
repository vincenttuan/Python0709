import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "demo"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)

        self.checkbutton = tk.Checkbutton(self)
        self.checkbutton["text"] = "demo"
        self.checkbutton.grid(row=1, column=0, sticky=tk.N + tk.W)

        self.entry = tk.Entry(self)
        self.entry.grid(row=2, column=0, sticky=tk.N + tk.W)

        self.label = tk.Label(self)
        self.label["text"] = "demo"
        self.label.grid(row=3, column=0, sticky=tk.N + tk.W)

        self.listbox = tk.Listbox(self)
        self.listbox["height"] = 5
        self.listbox.insert(1, "Python")
        self.listbox.insert(2, "Java")
        self.listbox.insert(3, "Swift")
        self.listbox.insert(4, "JavaScript")
        self.listbox.insert(5, "C")
        self.listbox.grid(row=4, column=0, sticky=tk.N + tk.W)

        self.optionList = ("Python", "Java", "Swift")
        self.v = tk.StringVar()
        self.v.set("demo")
        self.optionmenu = tk.OptionMenu(self, self.v, *self.optionList)
        self.optionmenu.grid(row=5, column=0, sticky=tk.N + tk.W)

        self.radiobutton = tk.Radiobutton(self)
        self.radiobutton["text"] = "demo"
        self.radiobutton.grid(row=6, column=0, sticky=tk.N + tk.W)

        self.scale = tk.Scale(self)
        self.scale.grid(row=7, column=0, sticky=tk.N + tk.W)

        self.spinbox = tk.Spinbox(self, from_=0, to=10)
        self.spinbox.grid(row=8, column=0, sticky=tk.N + tk.W)

        self.text = tk.Text(self)
        self.text["height"] = 10
        self.text["width"] = 50
        self.text.grid(row=9, column=0, sticky=tk.N + tk.W)


root = tk.Tk()
app = Application(root)
root.mainloop()