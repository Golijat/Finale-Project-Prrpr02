import requests

def coord(city):
    City = requests.get(f"https://geocode.maps.co/search?q={city}")
    City = City.json()
    City_Name = City[0]["display_name"]
    City_Lat = City[0]["lat"]
    City_Lon = City[0]["lon"]
    return City_Name, City_Lat, City_Lon