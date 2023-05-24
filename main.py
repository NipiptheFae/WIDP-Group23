from bs4 import BeautifulSoup
import requests


url = f"https://weather.com/tr-TR/weather/tenday/l/İzmir+İzmir?canonicalCityId=a3722d3ba43ddbef656021ba77ee61bf4c6fae20636732a1f2958d22beb70107"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="DailyContent--narrative--3Ti6_")
data = str(page_text).split("En ")[-1].split(".")[0].split()[-1]
print(data)