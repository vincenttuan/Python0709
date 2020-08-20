import tkinter
import tkinter.ttk as ttk

# GUI 視窗
win = tkinter.Tk()
win.title('GUI 元件視窗') # 視窗標頭
win.geometry("300x300")  # 視窗大小

# GUI 元件配置
# 標籤 Label
my_label = ttk.Label(win, text='我是標籤')
my_label.pack()


win.mainloop() # 視窗運行

