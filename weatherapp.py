import requests
from decouple import config

API_KEY = config('API_KEY')
URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = data["main"]["temp"]
    fahrenheit = round(((temperature-273.15) * 1.8) + 32, 1)
    print("Weather: ", weather)
    print("Temperature: ", fahrenheit,"F")
else:
    print("Error occurred")