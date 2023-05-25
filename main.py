import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from tkinter import *
import requests
import re

url = f"https://www.mynet.com/hava-durumu/izmir-haftalik-hava-durumu"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


def today():
    page_text1 = doc.find(class_="weather-list-box mx-3")

    nem1 = str(page_text1).split("Nem:")[1].split("</div>")[0]
    print(nem1)
    temps1 = str(page_text1).split("düşük:")[1].split("</div>")[0]
    print(temps1)
    yagis1 = str(page_text1).split("İhtimali: ")[1].split("</div>")[0]
    print(yagis1)
    rüzgar1 = str(page_text1).split("Rüzgar Hızı:")[1].split(" </div>")[0]
    print(rüzgar1)


def secondDay():
    page_text = doc.find(class_="d-flex weather-list-item-container")

    nem = str(page_text).split("Nem:</strong>")[1].split("</div>")[0]
    print(nem)
    temps = str(page_text).split("düşük:</strong>")[1].split("</div>")[0]
    print(temps)
    yagis = str(page_text).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    print(yagis)
    rüzgar = str(page_text).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]
    print(rüzgar)

def thirdDay():
    page_text = doc.findAll(class_="d-flex weather-list-item-container")
    day2= str(page_text).split("<strong>Hissedilen:</strong>")[2]

    nem = str(day2).split("Nem:</strong>")[1].split("</div>")[0]
    print(nem)
    temps = str(day2).split("düşük:</strong>")[1].split("</div>")[0]
    print(temps)
    yagis = str(day2).split("Yağış İhtimali:</strong>")[1].split(" </div>")[0]
    print(yagis)
    rüzgar = str(day2).split("Rüzgar Hızı:</strong>")[1].split(" </div>")[0]
    print(rüzgar)

today()
secondDay()
thirdDay()


###################       GUI
root = Tk()
root.title("Weather Information Display Program")
title = tk.Label(root, text='Welcome!')
title.pack()
title2 = tk.Label(root, text='Please choose your city.')
title2.pack()

def show():
        myLabel = Label(root,text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Ankara")

####        DROPDOWN LIST
drop = OptionMenu(root, clicked, "Ankara","Istanbul","Izmir","Bursa","Antalya","Konya","Adana","Sanliurfa","Gaziantep","Kocaeli")

confirmButton = Button(root,text="Confirm") #add command here!
drop.pack()

####        OPTION LIST
myButton = Button(root,text="Today", command=today).pack()
myButton2 = Button(root,text="Tomorrow", command=secondDay).pack()
myButton3 = Button(root,text="2 Days Later", command=thirdDay).pack()




root.mainloop()







