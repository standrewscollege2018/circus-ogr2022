# Import required files & packages
from tkinter import *
from tkinter import ttk

class Film:
    
    def __init__(self, name, price):
        self._name = name
        self._price = price
        films.append(self)
        names.append(name)
        print(self._name, self._price)

# update_label empties the label and then reloads it
def update_label():
    price_list.set("")
    for f in films:
        price_list.set(price_list.get() + f._name + "   $" + str(f._price) + "\n")

films = []
names = []

Film("Iron Man", 8)
Film("Ant Man", 4)
 
# Create the window and give it a title. Set window size to fit the display.
window = Tk()
window.title("RentFlix")
window.geometry('6000x5000')
 
#NoteBook Tabs / Frame Views
tab_control = ttk.Notebook(window)
# Create Frames
homePage = ttk.Frame(tab_control)
categories = ttk.Frame(tab_control)
adminHome = ttk.Frame(tab_control)
 
# Page Controls & Give labels
tab_control.add(homePage, text='Home')
tab_control.add(categories, text='Categorys')
tab_control.add(adminHome, text='Admin')
 
# Home Page Content
# set up a label to display menu
price_list = StringVar()
update_label()

menu_lbl = Label(homePage, textvariable=price_list).grid(row=0)
 
# Categories Content
lbl2 = Label(categories, text= 'Films')
lbl2.grid(column=0, row=0)

# Admin Dashboard
lbl3 = Label(adminHome, text= 'Add Film')
lbl3.grid(column=0, row=0)
lbl4 = Label(adminHome, text= 'Stock Film')
lbl4.grid(column=0, row=1)
lbl5 = Label(adminHome, text= 'Edit Film')
lbl5.grid(column=0, row=2)
 
# View / Tab Control
tab_control.pack(expand=1, fill='both')

# Inetiate the window
window.mainloop()