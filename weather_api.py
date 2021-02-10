import requests
import json
import credentials
from pprint import pprint

#declare a const that will be used in converting Kelvin degs into Celsius degs
ZERO_DEGREES_KELVIN = 273.15

#functions
def get_json_response(api_url, headers_params, parameters):
    response = requests.get(api_url, headers=headers_params, params=parameters)

    return response

def get_data_from_server(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        return "Nieprawidłowy format!"
    else:
        return content

#Ask user about city and country
city_country = input("Podaj miasto i kraj(np. Warszawa, pl): ")

#set up parameters
params = {
    'q': city_country,
    "lang": "pl"
}

#make a request  https://community-open-weather-map.p.rapidapi.com/weather credentials.headers params
response = get_json_response('https://community-open-weather-map.p.rapidapi.com/weather', credentials.headers, params)

# download data from rapidapis's server
content = get_data_from_server(response)

#test
# pprint(content)

#Download info about temperature
currentTemperatureInfo = content['main']

#default: Kelvin degrees, download info about current_temp, min_temp, max_temp and feels_like_temp
currentTemperatureKelvin = currentTemperatureInfo['temp']
feelsLikeTemperatureKelvin = currentTemperatureInfo['feels_like']
minTemperatureKelvin = currentTemperatureInfo['temp_min']
maxTemperatureKelvin = currentTemperatureInfo['temp_max']

#tests
# print(currentTemperatureKelvin)
# print(feelsLikeTemperatureKelvin)
# print(minTemperatureKelvin)
# print(maxTemperatureKelvin)

#convert Kelvin degs into Celsius degs
currentTemperatureCelsius = round((currentTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)
feelsLikeTempreatureCelsius = round((feelsLikeTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)
minTemperatureCelsius = round((minTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)
maxTemperatureCelsius = round((maxTemperatureKelvin - ZERO_DEGREES_KELVIN), 2)

#get info about description(weather)
weatherDescriptionContent = content['weather']
weatherDescription = weatherDescriptionContent[0]['description'].capitalize()

#display current temp and feels_like temp
print("Temperatura: " + str(currentTemperatureCelsius))
print("Temperatura odczuwalna: " + str(feelsLikeTempreatureCelsius))
print("Temperatura minimalna: " + str(minTemperatureCelsius))
print("Temperatura maksymalna: " + str(maxTemperatureCelsius))
print("Ogólne informacje o pogodzie: " + weatherDescription + ".")
    