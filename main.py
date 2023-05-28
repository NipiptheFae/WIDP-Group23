import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from tkinter import *
import requests
import re

temperature_unit = "Celsius"

def today():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text1 = doc.find(class_="weather-list-box mx-3")
    nem1 = str(page_text1).split("Nem:")[1].split("</div>")[0]
    # temp variable just holds morning temperature
    temp = str(page_text1).split("düşük:")[1].split("</div>")[0].split()[0]
    temps2 = str(page_text1).split("düşük:")[1].split("</div>")[0].split()[1]
    temps1 = temp + temps2
    # temp3 variable just holds night temperature
    temp3 = temps2.split("/")[1].split("°")[0]
    yagis1 = str(page_text1).split("İhtimali: ")[1].split("</div>")[0]
    rüzgar1 = str(page_text1).split("Rüzgar Hızı:")[1].split(" </div>")[0]


    weather_data = {
        "Humidity": nem1,
        "Temperature in the morning": temp,
        "Temperature at night": temp3,
        "Rain Possibility": yagis1,
        "Wind Speed": rüzgar1
    }

    display_weather_data(weather_data)


def secondDay():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text = doc.find(class_="d-flex weather-list-item-container")
    nem = str(page_text).split("Nem:</strong>")[1].split("</div>")[0]
    temps = str(page_text).split("düşük:</strong>")[1].split("</div>")[0]
    # temp1 variable just holds morning temperature
    temp1 = temps.split("/")[0].split("°")[0]
    # temp2 variable just holds night temperature
    temp2 = temps.split("/")[1].split("°")[0]
    yagis = str(page_text).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(page_text).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]

    weather_data = {
        "Humidity": nem,
        "Temperature in the morning": temp1,
        "Temperature at night": temp2,
        "Rain Possibility": yagis,
        "Wind Speed": rüzgar
    }

    display_weather_data(weather_data)


def thirdDay():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text = doc.findAll(class_="d-flex weather-list-item-container")
    day2 = str(page_text).split("<strong>Hissedilen:</strong>")[2]
    nem = str(day2).split("Nem:</strong>")[1].split("</div>")[0]
    temps = str(day2).split("düşük:</strong>")[1].split("</div>")[0]
    # temp1 variable just holds morning temperature
    temp1 = temps.split("/")[0].split("°")[0]
    # temp2 variable just holds night temperature
    temp2 = temps.split("/")[1].split("°")[0]
    yagis = str(day2).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(day2).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]

    weather_data = {
        "Humidity": nem,
        "Temperature in the morning": temp1,
        "Temperature at night": temp2,
        "Rain Possibility": yagis,
        "Wind Speed": rüzgar
    }

    display_weather_data(weather_data)


def display_weather_data(weather_data):
    space_label.config(text = "----------------------------------------------------------------------------------")
    nem_label.config(text="Humidity: " + weather_data["Humidity"], image=scaled_humidity_img, compound=LEFT)
    temps_morning_label.config(text="Temperature in the morning: " + weather_data["Temperature in the morning"], image=scaled_morning_img, compound=LEFT)
    temps_night_label.config(text="Temperature at night: " + weather_data["Temperature at night"], image=scaled_night_img, compound=LEFT)
    yagis_label.config(text="Rain Possibility: " + weather_data["Rain Possibility"], image=scaled_rain_img, compound=LEFT)
    rüzgar_label.config(text="Wind Speed: " + weather_data["Wind Speed"], image=scaled_wind_img, compound=LEFT)
    space2_label.config(text="---------------------------------------------")
    if temperature_unit == "Celsius":
        converted_temperature_morning = weather_data["Temperature in the morning"]
        converted_temperature_night = weather_data["Temperature at night"]
        temps_morning_label.config(text="Temperature in the morning: " + converted_temperature_morning + "° " + temperature_unit)
        temps_night_label.config(text="Temperature at night: " + converted_temperature_night + "° " + temperature_unit)

    else:
        temperature_morning = float(weather_data["Temperature in the morning"])
        temperature_night = float(weather_data["Temperature at night"])
        converted_temperature_morning = str((temperature_morning * 9 / 5) + 32)
        converted_temperature_night = str((temperature_night * 9 / 5) + 32)
        temps_morning_label.config(text="Temperature in the morning: " + converted_temperature_morning + "° " + temperature_unit)
        temps_night_label.config(text="Temperature at night: " + converted_temperature_night + "° " + temperature_unit)



def toggle_unit():
    global temperature_unit

    if temperature_unit == "Celsius":
        temperature_unit = "Fahrenheit"
    else:
        temperature_unit = "Celsius"

    unit_label.config(text="Temperature Unit: " + temperature_unit)
    space3_label.config(text="---------------------------------------------")



###################       GUI

root = Tk()
root.title("Weather Information Display Program")

root.geometry("800x700")

font_size = 14

#### Images
humidity_img = PhotoImage(file="C:\\Users\\alper\\Downloads\\nem.png")
scaled_humidity_img = humidity_img.subsample(3, 3)

morning_img = PhotoImage(file="C:\\Users\\alper\\Downloads\\morning.png")
scaled_morning_img = morning_img.subsample(3, 3)

night_img = PhotoImage(file="C:\\Users\\alper\\Downloads\\night.png")
scaled_night_img = night_img.subsample(8, 8)

rain_img = PhotoImage(file="C:\\Users\\alper\\Downloads\\yagis.png")
scaled_rain_img = rain_img.subsample(3, 3)

wind_img = PhotoImage(file="C:\\Users\\alper\\Downloads\\ruzgar.png")
scaled_wind_img = wind_img.subsample(3, 3)


title = tk.Label(root, text='Welcome!', font=("Arial", font_size))
title.pack()

title2 = tk.Label(root, text='Please choose your city.', font=("Arial", font_size))
title2.pack()

clicked = StringVar()
clicked.set("")

####        DROPDOWN LIST
drop = OptionMenu(root, clicked, "Ankara", "Istanbul", "Izmir", "Bursa", "Antalya", "Konya", "Adana", "Sanliurfa",
                  "Gaziantep", "Kocaeli")
drop.pack()

####        OPTION LIST

myButton = Button(root, text="Today", command=today, font=("Arial", font_size))
myButton.pack()

myButton2 = Button(root, text="Tomorrow", command=secondDay, font=("Arial", font_size))
myButton2.pack()

myButton3 = Button(root, text="2 Days Later", command=thirdDay, font=("Arial", font_size))
myButton3.pack()

space_label = Label(root, font=("Arial", font_size))
space_label.pack()

nem_label = Label(root, font=("Arial", font_size), image=scaled_humidity_img, compound=LEFT)
nem_label.pack()

temps_morning_label = Label(root, font=("Arial", font_size), image=scaled_morning_img, compound=LEFT)
temps_morning_label.pack()

temps_night_label = Label(root, font=("Arial", font_size), image=scaled_night_img, compound=LEFT)
temps_night_label.pack()

yagis_label = Label(root, font=("Arial", font_size), image=scaled_rain_img, compound=LEFT)
yagis_label.pack()

rüzgar_label = Label(root, font=("Arial", font_size), image=scaled_wind_img, compound=LEFT)
rüzgar_label.pack()

space2_label = Label(root, font=("Arial", font_size))
space2_label.pack()


unit_label = Label(root, font=("Arial", font_size))
unit_label.pack()

space3_label = Label(root, font=("Arial", font_size))
space3_label.pack()


toggle_button = Button(root, text="Toggle Temperature Unit", command=toggle_unit, font=("Arial", font_size))
toggle_button.pack()

root.mainloop()
