import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from tkinter import *
import requests
import re

def today():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text1 = doc.find(class_="weather-list-box mx-3")
    nem1 = str(page_text1).split("Nem:")[1].split("</div>")[0]
    temp = str(page_text1).split("düşük:")[1].split("</div>")[0].split()[0]
    temps2 = str(page_text1).split("düşük:")[1].split("</div>")[0].split()[1]
    temps1 = temp + temps2
    temp3 = temps2.split("/")[1].split("°")[0]
    yagis1 = str(page_text1).split("İhtimali: ")[1].split("</div>")[0]
    rüzgar1 = str(page_text1).split("Rüzgar Hızı:")[1].split(" </div>")[0]

    
    weather_data = {
        "Humidity": nem1,
        "Temperature": temps1,
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
    temp1 = temps.split("/")[0].split("°")[0]
    temp2 = temps.split("/")[1].split("°")[0]
    yagis = str(page_text).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(page_text).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]


    weather_data = {
        "Humidity": nem,
        "Temperature": temps,
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
    temp1 = temps.split("/")[0].split("°")[0]
    temp2 = temps.split("/")[1].split("°")[0]
    yagis = str(day2).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(day2).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]


    weather_data = {
        "Humidity": nem,
        "Temperature": temps,
        "Rain Possibility": yagis,
        "Wind Speed": rüzgar
    }


    display_weather_data(weather_data)


def display_weather_data(weather_data):

    nem_label.config(text="Humidity: " + weather_data["Humidity"])
    temps_label.config(text="Temperature: " + weather_data["Temperature"])
    yagis_label.config(text="Rain Possibility: " + weather_data["Rain Possibility"])
    rüzgar_label.config(text="Wind Speed: " + weather_data["Wind Speed"])


###################       GUI

root = Tk()
root.title("Weather Information Display Program")


root.geometry("500x400")


font_size = 14

title = tk.Label(root, text='Welcome!', font=("Arial", font_size))
title.pack()

title2 = tk.Label(root, text='Please choose your city.', font=("Arial", font_size))
title2.pack()

clicked = StringVar()
clicked.set("")

####        DROPDOWN LIST
drop = OptionMenu(root, clicked, "Ankara", "Istanbul", "Izmir", "Bursa", "Antalya", "Konya", "Adana", "Sanliurfa", "Gaziantep", "Kocaeli")
drop.pack()

####        OPTION LIST
myButton = Button(root, text="Today", command=today, font=("Arial", font_size))
myButton.pack()
myButton2 = Button(root, text="Tomorrow", command=secondDay, font=("Arial", font_size))
myButton2.pack()
myButton3 = Button(root, text="2 Days Later", command=thirdDay, font=("Arial", font_size))
myButton3.pack()


nem_label = Label(root, font=("Arial", font_size))
nem_label.pack()
temps_label = Label(root, font=("Arial", font_size))
temps_label.pack()
yagis_label = Label(root, font=("Arial", font_size))
yagis_label.pack()
rüzgar_label = Label(root, font=("Arial", font_size))
rüzgar_label.pack()

root.mainloop()
