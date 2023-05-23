"""
Class for fetching weather information
"""
import requests
class WeatherFetch:
    """
    This class is used to fetch weather info from the internet.
    """
    def __init__(self, lat, lon):
        self.cur_temp = 0
        self.cur_symbol = "NULL"
        self.next_six_temp = 0
        self.next_six_symbol = "NULL"
        self.lat = lat
        self.lon = lon

    def start(self):
        city = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/\
complete?lat={self.lat}&lon={self.lon}",
timeout = 10, headers={"User-Agent":"End-Projekt/0.0.1 github.com/Golijat/Finale-Project-Prrpr02"})
        city = city.json()
        self.cur_temp = city\
            ['properties']['timeseries'][0]["data"]["instant"]["details"]["air_temperature"]
        self.cur_symbol = city\
            ['properties']['timeseries'][0]["data"]["next_1_hours"]["summary"]["symbol_code"]

        self.next_six_temp = city['properties']\
            ['timeseries'][0]["data"]["next_6_hours"]["details"]["air_temperature_min"]
        self.next_six_symbol = city\
            ['properties']['timeseries'][0]["data"]["next_6_hours"]["summary"]["symbol_code"]

    def curTemp(self):
        return self.cur_temp
    def curSymbol(self):
        return self.cur_symbol
    def nextSixTemp(self):
        return self.next_six_temp
    def nextSixSymbol(self):
        return self.next_six_symbol
