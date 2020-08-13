# OpenWeather
import tkinter
import datetime
import requests
import json

def update():
    path = 'https://api.openweathermap.org/data/2.5/weather?q=Taoyuan,TW&appid=fcc57465b76d35357c84e4e30fe2431a'
    ow = json.loads(requests.get(path).text)
    temp = ow['main']['temp'] - 273.15
    feels_like = ow['main']['feels_like'] - 273.15
    humidity = ow['main']['humidity']
    weatherMain = ow['weather'][0]['main']
    ans.set("氣溫: %.2f°C\n體感: %.2f°C\n濕度: %.2f%%\n%s" % (temp, feels_like, humidity, weatherMain))

win = tkinter.Tk()
win.title("Taoyuan(桃園)天氣")
win.geometry("300x200")

ans = tkinter.StringVar()
update()

label = tkinter.Label(win, textvariable=ans)
label.config(font=("Arial", 20))
label.pack()

addButton = tkinter.Button(win, text="Update", command=update)
addButton.config(font=("Arial", 20))
addButton.pack()

win.mainloop()