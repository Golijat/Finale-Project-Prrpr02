"""
GUI.py handles the Graphical User Interface that displays the weather information.
"""
from tkinter import Tk, Label, END, Toplevel, Button, Entry
#Tk, Label, Frame
# from tkinter import ttk
from coordinates import coord
from weather_fetch import WeatherFetch
from city_list_gui import ChooseCity
from blocks import TopBlock


root = Tk()
root.title("Weather For You")
#Sets Title
root.geometry("500x500")
#Sets the size of the gui window
top = TopBlock("blue", 75, 5)

print()
topLabel = Label(background=top.bg_color, width=top.size)
topLabel.grid(row=0, column=1, columnspan= top.span)

# Sends in the city name searched for into the coordinates function
# The function returns the city name and it's coordinates
# Then the coordinates are sent into the display weather class.

# This function is used to allow a user to more precisley
# select the place they want weather information for.
# The function gets all the cities that can be found from the input the user makes.
# Then a new window opens where the user can click on the city they want and then
# the coordinates for that specific place is used.
def search_for_city(city_name):
    """
    Uses the city name given to open a popup window
    where the user can choose from a number of
    cities with names of the name given or similar to it.
    The button that is clicked returns it's id
    which is used to send coordinates to an api
    that returns the weather for that place.
    Then that weather is displayed on screen.
    """
    # First the display labels and search entry field is cleared.
    search_bar.delete(0, END)
    city_name_display_label.configure(text="")
    current_display_label.configure(text="")
    current_weather_display_label.configure(text="")
    next_six_hours_display_label.configure(text="")
    next_six_hours_weather_display_label.configure(text="")

    # Checks weather something has been put into the entry field.
    # If not it exits the function.
    if city_name == "":
        print("No name given")
        return
    try:
        # Sends in the city name into a function that gets all the cities/places
        # that have that name or a name similar to it and puts all those cities
        # and their coordinates into a list that is returned.
        city_list = coord(city_name)

        # If no place with the city name exists, then nothing is returend
        # and the except function goes into effect.
        if city_list == []:
            current_weather_display_label.configure(text="City searched for does not exist")

        # Opens a new window where the user can choose the specifc city
        # that they want.
        scroot = Toplevel(root)
        # Creates a class that has the window root and
        # the list of cities.
        choose = ChooseCity(scroot, city_list)
        # The ChooseCity buttons method is activated and the
        # code is orderd to wait for it to finish.
        choose.buttons()
        # Code is orderd to wait.
        root.wait_window(scroot)

        # After the buttons method is finished the id
        # that was chosen from the buttons function is
        # taken and put into a variable.
        value = choose.get_id()

        # The id is used to get the specic name and coordinates that the user wanted
        # and sends them into the display_weather function.
        display_weather(city_list[value].lat, city_list[value].lon, city_list[value].name)
    except:
        # If something goes wrong with getting a list of cities and opening a new window
        # then an error message is displayed.
        city_name_display_label.configure(text="An Error Occured, please try again")

def display_weather(lat, lon, name):
    """
    Displays the weather by changing the text
    of a few labels.
    """
    fetch = WeatherFetch(lat,lon)
    fetch.start()
    current_weather_display_label.configure(text=f"{fetch.curTemp()} {fetch.curSymbol()}")
    next_six_hours_weather_display_label.configure(text=f"{fetch.nextSixTemp()} {fetch.nextSixSymbol()}")
    city_name_display_label.configure(text=name)
    current_display_label.configure(text="Current Weather")
    next_six_hours_display_label.configure(text="Next Six Hours Weather")

# Used to write the words "Current Weather" over
# the current weather.
current_display_label = Label(root, text="")
current_display_label.grid(row=3, column=1)

# Used to write the words "Next Six Hours Weather"
# over the next six hours weather.
next_six_hours_display_label = Label(root, text="")
next_six_hours_display_label.grid(row=5, column=1)

# Used to display the current weather on screen.
current_weather_display_label = Label(root, text="")
current_weather_display_label.grid(row=4,column=1)

# Used to display the next six hours weather on screen.
next_six_hours_weather_display_label = Label(root, text="")
next_six_hours_weather_display_label.grid(row=6,column=1)

# Used to display the city name over the cities weather on screen.
city_name_display_label = Label(root, text="")
city_name_display_label.grid(row=2,column=1)

search_bar = Entry(root)
search_bar.grid(row=1, column=1) #columnspan=3

search_button = Button(root, text="search", command=lambda:search_for_city(search_bar.get()))
search_button.grid(row=1,column=2)

root.mainloop()
