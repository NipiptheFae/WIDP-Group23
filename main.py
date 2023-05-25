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
    temps1 = str(page_text1).split("düşük:")[1].split("</div>")[0]
    yagis1 = str(page_text1).split("İhtimali: ")[1].split("</div>")[0]
    rüzgar1 = str(page_text1).split("Rüzgar Hızı:")[1].split(" </div>")[0]

    # Display the results in GUI labels
    nem_label.config(text=nem1)
    temps_label.config(text=temps1)
    yagis_label.config(text=yagis1)
    rüzgar_label.config(text=rüzgar1)

def secondDay():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text = doc.find(class_="d-flex weather-list-item-container")
    nem = str(page_text).split("Nem:</strong>")[1].split("</div>")[0]
    temps = str(page_text).split("düşük:</strong>")[1].split("</div>")[0]
    yagis = str(page_text).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(page_text).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]

    # Display the results in GUI labels
    nem_label.config(text=nem)
    temps_label.config(text=temps)
    yagis_label.config(text=yagis)
    rüzgar_label.config(text=rüzgar)

def thirdDay():
    clicked_city = clicked.get()
    url = f"https://www.mynet.com/hava-durumu/{clicked_city}-haftalik-hava-durumu"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text = doc.findAll(class_="d-flex weather-list-item-container")
    day2 = str(page_text).split("<strong>Hissedilen:</strong>")[2]
    nem = str(day2).split("Nem:</strong>")[1].split("</div>")[0]
    temps = str(day2).split("düşük:</strong>")[1].split("</div>")[0]
    yagis = str(day2).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    rüzgar = str(day2).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]

    # Display the results in GUI labels
    nem_label.config(text=nem)
    temps_label.config(text=temps)
    yagis_label.config(text=yagis)
    rüzgar_label.config(text=rüzgar)


###################       GUI

root = Tk()
root.title("Weather Information Display Program")

title = tk.Label(root, text='Welcome!')
title.pack()

title2 = tk.Label(root, text='Please choose your city.')
title2.pack()

clicked = StringVar()
clicked.set("")

####        DROPDOWN LIST
drop = OptionMenu(root, clicked, "Ankara", "Istanbul", "Izmir", "Bursa", "Antalya", "Konya", "Adana", "Sanliurfa", "Gaziantep", "Kocaeli")
drop.pack()

####        OPTION LIST
myButton = Button(root,text="Today", command=today).pack()
myButton2 = Button(root,text="Tomorrow", command=secondDay).pack()
myButton3 = Button(root,text="2 Days Later", command=thirdDay).pack()

# Labels to display the results
nem_label = Label(root)
nem_label.pack()
temps_label = Label(root)
temps_label.pack()
yagis_label = Label(root)
yagis_label.pack()
rüzgar_label = Label(root)
rüzgar_label.pack()

root.mainloop()
