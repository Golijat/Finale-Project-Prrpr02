import requests
from city_button_list import City

def coord(city):
    city = requests.get(f"https://geocode.maps.co/search?q={city}")
    city = city.json()
    city_list = []
    for i in range(0, len(city)):
        city_list.append(City(city[i]["display_name"], city[i]["lat"], city[i]["lon"]))
        # Uses the city_button_list class to put the name, lat and lon of all cities from the geocode api in a list.
        # Then a person can use the list to get the information.
    return city_list