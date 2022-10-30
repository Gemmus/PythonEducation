# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation.
# You must register for the service to receive the API key required for making API requests.
# Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests
import json

municipality = input("Please enter the municipality: ")

request = "https://api.tvmaze.com/search/shows?q=" + municipality
response = requests.get(request).json()
print(response)
# or:
print(json.dumps(response, indent=2))
# or:
for a in response:
    print(a["show"]["name"])
# or:
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

# C = K - 273.15 K = C + 273.15