import requests
import json
import credentials
from pprint import pprint

ZERO_DEGREES_KELVIN = 273.15

city_country = input("Podaj miasto i kraj(np. Warsaw, pl)")

params = {
    'q': city_country
}

response = requests.get('https://community-open-weather-map.p.rapidapi.com/weather', headers=credentials.headers, params=params)

try:
    content = response.json()
except json.decoder.JSONDecodeError:
    print("Nieprawidłowy format!")
else:
    # pprint(content)
    currentTemperatureInfo = content['main']

    currentTemperatureKelvin = currentTemperatureInfo['temp']
    feelsLikeTemperatureKelvin = currentTemperatureInfo['feels_like']

    # print(currentTemperatureKelvin)
    # print(feelsLikeTemperatureKelvin)

    currentTemperatureCelsius = round((currentTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)
    feelsLikeTempreatureCelsius = round((feelsLikeTemperatureKelvin - ZERO_DEGREES_KELVIN))

    print("Temperatura: " + str(currentTemperatureCelsius))
    print("Temperatura odczuwalna: " + str(feelsLikeTempreatureCelsius))
    