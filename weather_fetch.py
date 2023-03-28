"""
Class for fetching weather information
"""
import requests

Arvika = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/\
complete?lat=59.516667&lon=13.8",
timeout = 10, headers={"User-Agent":"End-Projekt/0.0.1 github.com/Golijat/Finale-Project-Prrpr02"})
Arvika = Arvika.json()
arvika_temp = Arvika['properties']['timeseries'][0]["data"]["instant"]["details"]["air_temperature"]
print(arvika_temp)