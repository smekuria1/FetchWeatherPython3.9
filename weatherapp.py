import requests
from decouple import config

#Get api key from .env file
API_KEY = config('API_KEY')
#Target Url
URL = "http://api.openweathermap.org/data/2.5/weather"
#UI
city = input("Enter a city name: ")

#url for api request
request_url = f"{URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#output
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = data["main"]["temp"]
    fahrenheit = round(((temperature-273.15) * 1.8) + 32, 1) #conversion and rounding
    print("Weather: ", weather)
    print("Temperature: ", fahrenheit,"F")
else:
    print("Error occurred")