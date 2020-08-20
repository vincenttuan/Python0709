import tkinter
import tkinter.ttk as ttk

def ctof():
    c = float(my_entry_c.get())
    f = c * 9/5 + 32
    f_value.set(f)
    print(c, type(c), f)

def ftoc():
    f = float(my_entry_f.get())
    c = (f-32) * 5/9
    c_value.set(c)
    print(f, type(f), c)

# GUI 視窗
win = tkinter.Tk()
win.title('攝氏華氏轉換') # 視窗標頭
win.geometry("400x100")  # 視窗大小

s = ttk.Style()
s.configure('My.TButton', font=('Arial', 15))

# 建立窗框
my_frame_c = ttk.Frame(win)
my_frame_f = ttk.Frame(win)
my_frame_c.pack()
my_frame_f.pack()

# GUI 元件建立
# 標籤 Label
my_label_c = ttk.Label(my_frame_c, text='攝氏', font=('Arial', 15))
my_label_f = ttk.Label(my_frame_f, text='華氏', font=('Arial', 15))
# 輸入框
c_value = tkinter.DoubleVar() # 建立變數
c_value.set(0)
f_value = tkinter.DoubleVar()
f_value.set(0)
my_entry_c = ttk.Entry(my_frame_c, textvariable=c_value, font=('Arial', 15))
my_entry_f = ttk.Entry(my_frame_f, textvariable=f_value, font=('Arial', 15))
# 按鈕 Button
my_button_c = ttk.Button(my_frame_c, text='轉換', style='My.TButton', command=ctof)
my_button_f = ttk.Button(my_frame_f, text='轉換', style='My.TButton', command=ftoc)

# 元件配置
my_label_c.pack(side=tkinter.LEFT)
my_entry_c.pack(side=tkinter.LEFT)
my_button_c.pack(side=tkinter.LEFT)
my_label_f.pack(side=tkinter.LEFT)
my_entry_f.pack(side=tkinter.LEFT)
my_button_f.pack(side=tkinter.LEFT)

win.mainloop()