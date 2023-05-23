"""
A function that takes the name of a city, sends it
into an api and gets back all cities with names
equal to that sent in or similar to it.
"""

import requests
from city_button_list import City

def coord(city):
    """
    This function takes the name of a city sends it into an api
    and puts the result that gets sent back into a list.
    But only the city name and its coordinates are put
    into the list. The the list is returned to the caller of
    the function.
    """
    city = requests.get(f"https://geocode.maps.co/search?q={city}", timeout=10)
    city = city.json()
    city_list = []
    for i in range(0, len(city)):
        city_list.append(City(city[i]["display_name"], city[i]["lat"], city[i]["lon"]))
        # Uses the city_button_list class to put the name,
        # lat and lon of all cities from the geocode api in a list.
        # Then a person can use the list to get the information.
    return city_list
