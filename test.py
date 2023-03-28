"""
A test file for testing things
"""
# import json
# from bs4 import BeautifulSoup
import requests

print("Hello World!")

for i in range(0,10):
    print("Echo")


Arvika = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/\
complete?lat=59.516667&lon=13.8",
timeout = 10, headers={"User-Agent":"End-Projekt/0.0.1 github.com/Golijat/Finale-Project-Prrpr02"})
print(Arvika)
Arvika = Arvika.json()
arvika_temp = Arvika['properties']['timeseries'][0]["data"]["instant"]["details"]["air_temperature"]
print(arvika_temp)

# # currenthour_Arvika = requests.get("https://www.yr.no/api/v0/\
# # locations/2-2725123/forecast/currenthour", timeout = 10)
# currenthour = currenthour_Arvika.json()
# arvika_temp = currenthour['temperature']['value']
# arvika_weather = currenthour['symbolCode']["next1Hour"]
# print(f"The temperature right now in Arvika is {arvika_temp}\
#  degrees Celcius and the weather is {arvika_weather}.")
