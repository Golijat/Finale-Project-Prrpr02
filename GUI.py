from tkinter import *

root = Tk()
root.title("Weather For You")

for i in range(1,5):
    for g in range(0,3):
            myLabel = Label(root, text="Test")
            myLabel.grid(row=i,column=g)

test_label = Label(root, text="Test Label For GUI")
test_label.grid(row=2,column=1)

root.mainloop()