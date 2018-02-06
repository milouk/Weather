import requests
import json
import pytemperature
import tkinter as tk
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

#Gets Weather
def temperature():
    error_label.pack()
    error_label.pack_forget()
    try:
        req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city_name.get() + "," + country_code.get() + "&appid=replacewithyourapikey")
        tmp = req.json()['main']['temp']
        min_tmp = req.json()["main"]["temp_min"]
        max_tmp = req.json()["main"]["temp_max"]
        status = req.json()["weather"][0]["main"]
        icon = req.json()["weather"][0]["icon"]
        weather_icon_url = "http://openweathermap.org/img/w/" + icon + ".png"
        open_url = urlopen(weather_icon_url)
        weather_icon = io.BytesIO(open_url.read())
        pil_img = Image.open(weather_icon)
        weath_icon = ImageTk.PhotoImage(pil_img)
        weather_label.config(image = weath_icon)
        city_label.config(text = "Weather in " + city_name.get().capitalize())
        weather_label.image = weath_icon
        c_tmp_label.config(text ="\nCurrent Temperature is:  %s" % round(pytemperature.k2c(tmp), 1))
        min_tmp_label.config(text = "\nMinimum Temperature is:  %s" % round(pytemperature.k2c(min_tmp), 1))
        max_tmp_label.config(text = "\nMaximum Temperature is:  %s" % round(pytemperature.k2c(max_tmp), 1))
        weath_desc_label.config(text = "\nWeather Description:  %s\n" % (status))
        city_label.pack()
        weather_label.pack()
        c_tmp_label.pack()
        min_tmp_label.pack()
        max_tmp_label.pack()
        weath_desc_label.pack()
    except Exception:
        error_label.pack()


window = tk.Tk()
window.title("Weather")
window.geometry("500x450")
window.configure(background = 'black')
window.resizable(0, 0)

tk.Label(window, text = "Enter Country Code", bg='black', fg = 'white').pack(pady = '10')
country_code = tk.Entry(window, width = 40)
country_code.pack()
country_code.focus_set()
tk.Label(window, text = "Enter City Name", bg='black', fg = 'white').pack(pady = '10')
city_name = tk.Entry(window, width =  40)
city_name.pack()
weather_label = tk.Label(window, image = "", bg = 'black')
city_label = tk.Label(window, text = "", font = 'bold', bg='black', fg = 'white')
c_tmp_label = tk.Label(window, text = "", bg='black', fg = 'white')
min_tmp_label = tk.Label(window, text = "", bg='black', fg = 'white')
max_tmp_label = tk.Label(window, text = "", bg='black', fg = 'white')
weath_desc_label = tk.Label(window, text = "", bg='black', fg = 'white')
error_label = tk.Label(window, text = "Wrong Country Code or City Name, Please try again!", bg = 'black', fg = 'red', font = 'bold')
tk.Button(window, text = "Show weather", command = temperature, default='active', bg='white', fg = 'black', width = '20', pady = '5').pack(pady = '10')
window.mainloop()
