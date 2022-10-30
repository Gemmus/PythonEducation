# Write a program that fetches and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.

import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])
