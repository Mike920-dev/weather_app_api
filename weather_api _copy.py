import requests
import json
import credentials
from pprint import pprint

#declare a const that will be used in converting Kelvin degs into Celsius degs
ZERO_DEGREES_KELVIN = 273.15

#Ask user about city and country
city_country = input("Podaj miasto i kraj(np. Warszawa, pl): ")

#set up parameters
params = {
    'q': city_country,
    "lang": "pl"
}

#make a request  https://community-open-weather-map.p.rapidapi.com/weather credentials.headers params
response = requests.get('https://community-open-weather-map.p.rapidapi.com/weather', headers=credentials.headers, params=params)

try:
    content = response.json()
except json.decoder.JSONDecodeError:
    print("Nieprawidłowy format!")
else:
    pprint(content)
    #Download info about temperature
    currentTemperatureInfo = content['main']

    #default: Kelvin degrees, download info about current temp and feels_like temp  
    currentTemperatureKelvin = currentTemperatureInfo['temp']
    feelsLikeTemperatureKelvin = currentTemperatureInfo['feels_like']

    #tests
    # print(currentTemperatureKelvin)
    # # print(feelsLikeTemperatureKelvin)

    #convert Kelvin degs into Celsius degs
    currentTemperatureCelsius = round((currentTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)
    feelsLikeTempreatureCelsius = round((feelsLikeTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)

    #display current temp and feels_like temp
    print("Temperatura: " + str(currentTemperatureCelsius))
    print("Temperatura odczuwalna: " + str(feelsLikeTempreatureCelsius))
    # test = content['weather']

    # print(test[0]['description'])