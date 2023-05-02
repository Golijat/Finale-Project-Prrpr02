"""
Class for fetching weather information
"""
import requests

Arvika = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/\
complete?lat=59.516667&lon=13.8",
timeout = 10, headers={"User-Agent":"End-Projekt/0.0.1 github.com/Golijat/Finale-Project-Prrpr02"})
Arvika = Arvika.json()
arvika_temp = Arvika['properties']['timeseries'][0]["data"]["instant"]["details"]["air_temperature"]
# print(arvika_temp)

class Fetch:
    def __init__(self, lat, lon):
        self.cur_temp = 0
        self.cur_symbol = "NULL"
        self.next_six_temp = 0
        self.next_six_symbol = "NULL"
        self.lat = lat
        self.lon = lon

    def start(self):
        City = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/\
complete?lat={self.lat}&lon={self.lon}",
timeout = 10, headers={"User-Agent":"End-Projekt/0.0.1 github.com/Golijat/Finale-Project-Prrpr02"})
        City = City.json()
        
        self.cur_temp = City['properties']['timeseries'][0]["data"]["instant"]["details"]["air_temperature"]
        self.cur_symbol = City['properties']['timeseries'][0]["data"]["next_1_hours"]["summary"]["symbol_code"]

        self.next_six_temp = City['properties']['timeseries'][0]["data"]["next_6_hours"]["details"]["air_temperature_min"]
        self.next_six_symbol = City['properties']['timeseries'][0]["data"]["next_6_hours"]["summary"]["symbol_code"]
        print("Test")

    def curTemp(self):
        return self.cur_temp
    def curSymbol(self):
        return self.cur_symbol
    def nextSixTemp(self):
        return self.next_six_temp
    def nextSixSymbol(self):
        return self.next_six_symbol
    
    def prin(self):
        print("Här är vädret", self.cur_temp, self.cur_symbol, self.next_six_temp, self.next_six_symbol)

x = "z"
print("Hej {}".format(x))
fetch = Fetch(59.516667, 13.8)
fetch.start()
fetch.prin()

print(fetch.nextSixTemp())