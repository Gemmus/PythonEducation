# Familiarize yourself with the OpenWeather weather API.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.

import requests
import math


def get_weather(api, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    response = requests.get(url).json()
    temperature = response['main']['temp']
    return temperature - 273.15


def rounding(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n*multiplier+0.5)/multiplier


city_name = input("Please enter the municipality(City,CountryCode): ")
api_key = "628dc836c467279560786b9ec5b2a731"
celsius_degree = get_weather(api_key, city_name)
# print(celsius_degree)
celsius = rounding(celsius_degree)
print(f"It is currently {celsius:.0f}°C in {city_name}.")
