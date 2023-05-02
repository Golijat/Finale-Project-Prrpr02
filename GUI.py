"""
GUI.py handles the Graphical User Interface that displays the weather information.
"""
from tkinter import * #Tk, Label, Frame
# from tkinter import ttk
from coordinates import coord
from weather_fetch import Fetch


root = Tk()
root.title("Weather For You")

root.geometry("500x500")

for i in range(1,5):
    for g in range(0,3):
        myLabel = Label(root, text="Test")
        myLabel.grid(row=i,column=g)

test_label = Label(root, text="Test Label For GUI")
test_label.grid(row=2,column=1)

test_text = Label(text="Den du")

# Sends in the city name searched for into the coordinates function
# The function returns the city name and it's coordinates
# Then the coordinates are sent into the display weather class.

def search_for_city(city):
    search_bar.delete(0, END)
    if city == "":
        print("No name given")
        return
    print(coord(city))
    print(coord(city)[1])
    display_weather(coord(city)[1], coord(city)[2])

def display_weather(lat, lon):
    fetch = Fetch(lat,lon)
    fetch.start()
    weather = Label(root, text="")
    weather.configure(text=f"{fetch.curTemp()} {fetch.curSymbol()}")
    # weather = Label(root, text=f"{fetch.curTemp()} {fetch.curSymbol()}")
    weather.grid(row=3,column=1)

search_bar = Entry(root)
search_button = Button(root, text="search", command=lambda:search_for_city(search_bar.get()))
search_bar.grid(row=1, column=1)
search_button.grid(row=1,column=2)

root.mainloop()
