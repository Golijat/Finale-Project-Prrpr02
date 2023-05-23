"""
Class used to store information about cities.
Used in the search pop up window.
"""

class City:
    """
    The class is used to more easily
    store information about a city
    and make it easier to call for
    the information.
    """
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon