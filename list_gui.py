"""
The class is used to manage a popup window where
the user can pick the city they want.
"""
from tkinter import Button
class ChooseCity:
    """
    The class is used to handle a window
    that pops up when somebody uses the
    search function of the main window.
    """
    def __init__(self, scroot, city_list):
        self.scroot = scroot
        self.city_list = city_list
        self.city_id = 0
        self.scroot.title("City Select")
        self.scroot.geometry("500x500")
    def buttons(self):
        """
        Makes buttons appear.
        """
        for i in range(0, len(self.city_list)):
            Button(self.scroot, text=self.city_list[i].name,\
                   command=lambda i=i:self.select(i)).pack()

    def select(self, i):
        """
        Changes the city id and closes the pop up
        window.
        """
        self.city_id = i
        self.scroot.destroy()

    def get_id(self):
        """
        Returns the city id.
        """
        return self.city_id
