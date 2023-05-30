
import ttkbootstrap as ttkbootstrap
from bs4 import BeautifulSoup
from tkinter import *
import requests
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox

temperature_unit = "Celsius"

def save_settings():
    with open("Settings.txt", "w") as f:
        f.write(f"{temperature_unit}\n{clicked.get()}")

def load_settings():
    try:
        with open("Settings.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 2:
                global temperature_unit
                temperature_unit = lines[0].strip()
                clicked.set(lines[1].strip())
    except FileNotFoundError:
        pass


def on_program_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    save_settings()

def today():
    try:
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

        if temperature_unit == "Celsius":
            with open("Settings.txt", "w") as f:
                f.write("Celsius\n " + clicked_city)
        elif temperature_unit == "Fahrenheit":
            with open("Settings.txt", "w") as f:
                f.write("Fahrenheit\n" + clicked_city)
    except (requests.exceptions.RequestException, IndexError):
        messagebox.showerror("Error",
                             "Failed to get weather data. Please check your internet connection.")
    weather_data = {
        "Humidity": nem1,
        "Temperature in the morning": temp,
        "Temperature at night": temp3,
        "Rain Possibility": yagis1,
        "Wind Speed": rüzgar1
    }
    display_weather_data(weather_data)


def secondDay():
    try:
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

        if temperature_unit == "Celsius":
            with open("Settings.txt", "w") as f:
                f.write("Celsius\n " + clicked_city)
        elif temperature_unit == "Fahrenheit":
            with open("Settings.txt", "w") as f:
                f.write("Fahrenheit\n" + clicked_city)
    except (requests.exceptions.RequestException, IndexError):
        messagebox.showerror("Error",
                             "Failed to get weather data. Please check your internet connection.")

    weather_data = {
        "Humidity": nem,
        "Temperature in the morning": temp1,
        "Temperature at night": temp2,
        "Rain Possibility": yagis,
        "Wind Speed": rüzgar
    }

    display_weather_data(weather_data)


def thirdDay():
    try:
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

        if temperature_unit == "Celsius":
            with open("Settings.txt", "w") as f:
                f.write("Celsius\n " + clicked_city)
        elif temperature_unit == "Fahrenheit":
            with open("Settings.txt", "w") as f:
                f.write("Fahrenheit\n" + clicked_city)
    except (requests.exceptions.RequestException, IndexError):
        messagebox.showerror("Error",
                             "Failed to get weather data. Please check your internet connection.")

    weather_data = {
        "Humidity": nem,
        "Temperature in the morning": temp1,
        "Temperature at night": temp2,
        "Rain Possibility": yagis,
        "Wind Speed": rüzgar
    }

    display_weather_data(weather_data)


def display_weather_data(weather_data):

    humidity_label.config(text="Humidity: " + weather_data["Humidity"], image=humidity_img, compound=LEFT)
    temps_morning_label.config(text="Temperature in the morning: " + weather_data["Temperature in the morning"], image=morning_img, compound=LEFT)
    temps_night_label.config(text="Temperature at night: " + weather_data["Temperature at night"], image=night_img, compound=LEFT)
    rain_label.config(text="Rain Possibility: " + weather_data["Rain Possibility"], image=rain_img, compound=LEFT)
    wind_label.config(text="Wind Speed: " + weather_data["Wind Speed"], image=wind_img, compound=LEFT)

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
        unit_label.config(text="Temperature Unit: " + temperature_unit)

    else:
        temperature_unit = "Celsius"
        unit_label.config(text="Temperature Unit: " + temperature_unit)






###################       GUI

root = Tk()
root.title("Weather Information Display Program")
weather_img = ImageTk.PhotoImage(Image.open("weather.png"))
root.iconphoto(False, weather_img)
root.geometry("900x900")

font_size = 14

png_label = ttkbootstrap.Label(root, image= weather_img)
png_label.pack(side=TOP)



#### Images

hum_image = Image.open("humidity.png")
hum_image_size = (70, 50)
resized_hum_image = hum_image.resize(hum_image_size)
humidity_img = ImageTk.PhotoImage(resized_hum_image)

m_image = Image.open("morning.png")
m_image_size = (70, 50)
resized_m_image = m_image.resize(m_image_size)
morning_img = ImageTk.PhotoImage(resized_m_image)

n_image = Image.open("night.png")
n_image_size = (50, 30)
resized_n_image = n_image.resize(n_image_size)
night_img = ImageTk.PhotoImage(resized_n_image)

r_image = Image.open("rain.png")
r_image_size = (90, 50)
resized_r_image = r_image.resize(r_image_size)
rain_img = ImageTk.PhotoImage(resized_r_image)

w_image = Image.open("wind.png")
w_image_size = (70, 50)
resized_wind_image = w_image.resize(w_image_size)
wind_img = ImageTk.PhotoImage(resized_wind_image)


title = ttkbootstrap.Label(root, text='Welcome to Weather Information Display Program !', font=("Arial", font_size), background="pink")
title.pack()

title2 = ttkbootstrap.Label(root, text='Please choose your city.', font=("Arial", font_size), background="pink")
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
space_label.config(text = "----------------------------------------------------------------------------------")
space_label.pack()

humidity_label = Label(root, font=("Arial", font_size), image=humidity_img, compound=LEFT)
humidity_label.pack()

temps_morning_label = Label(root, font=("Arial", font_size), image=morning_img, compound=LEFT)
temps_morning_label.pack()

temps_night_label = Label(root, font=("Arial", font_size), image=night_img, compound=LEFT)
temps_night_label.pack()

rain_label = Label(root, font=("Arial", font_size), image=rain_img, compound=LEFT)
rain_label.pack()

wind_label = Label(root, font=("Arial", font_size), image=wind_img, compound=LEFT)
wind_label.pack()

space2_label = Label(root, font=("Arial", font_size))
space2_label.config(text = "----------------------------------------------------------------------------------")
space2_label.pack()


unit_label = Label(root, font=("Arial", font_size))
unit_label.pack()
unit_label.config(text="Temperature Unit: " + temperature_unit)

space3_label = Label(root, font=("Arial", font_size))
space3_label.config(text="---------------------------------------------")
space3_label.pack()


toggle_button = Button(root, text="Toggle Temperature Unit", command=toggle_unit, font=("Arial", font_size))
toggle_button.pack()

exitButton = Button(root, text="Exit Program", command= on_program_exit,font=("Arial", font_size))
exitButton.pack()


load_settings()
root.protocol("WM_DELETE_WINDOW", on_program_exit)

root.mainloop()
