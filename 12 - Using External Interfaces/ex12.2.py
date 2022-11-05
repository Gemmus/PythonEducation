# Familiarize yourself with the OpenWeather weather API.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.

import requests

city_name = input("Please enter the municipality(City,CountryCode): ")
api_key = "628dc836c467279560786b9ec5b2a731"


def get_weather(api, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

    response = requests.get(url).json()
    temp = response['main']['temp']
    celsius = temp - 273.15
    print(f"It is currently {celsius:4.2f}°C in {city}.")


get_weather(api_key, city_name)
