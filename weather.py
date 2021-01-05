import requests
from datetime import datetime, date
import random

today_weekday = date.today().strftime("%Y-%m-%d, %A")	# nazwy dni tygodnia
time = datetime.today().strftime("%H:%M")
city = 'katowice'
headers = {
    'x-rapidapi-key': "7ad25462ecmshfc519d0047cbca9p1ea5f5jsnc13500c50fef",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
           }
r = requests.get("https://community-open-weather-map.p.rapidapi.com/weather?q="+city+"%2Cpl&lang=pl&units=%22metric%22%20", headers=headers)
tasks = r.json()

temp = 300 - int (tasks['main']['temp'])
pressure = tasks['main']['pressure']

r = requests.get("https://type.fit/api/quotes?fbclid=IwAR0IdRKLDMkEvZc8UrEFpZm6EzvoaTrVRrAAtPRgBjawN78GciLamB7l_DA")
tasks = r.json()


note= random.choice(tasks)

print(city.title(),',',today_weekday,' godzina ',time, ', Temperatura: ', temp, 'C, Ciśnienie: ', pressure, 'hPa')
print(note['text'])
print(note['author'])