import tkinter
import tkinter.ttk as ttk

# GUI 視窗
win = tkinter.Tk()
win.title('GUI 元件視窗') # 視窗標頭
win.geometry("300x300")  # 視窗大小

# GUI 元件配置
# 標籤 Label
my_label = ttk.Label(win, text='我是標籤')
my_label.pack()  # 放置元件

# 按鈕 Button
my_button = ttk.Button(win, text='我是按鈕')
my_button.pack()


win.mainloop() # 視窗運行

