# -----------------------------
#         IMPORTED
#         CONTENT
# -----------------------------

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# -----------------------------
#          BACKEND 
# -----------------------------

class Film:
    
    def __init__(self, name, price, stock, num_sold):
        self._name = name
        self._price = price
        self._stock = stock
        self._num_sold = num_sold
        films.append(self)
        film_names.append(self._name)

    def _update_price(self, price):
        self._price = price

    def _update_stock(self, new_stock):
        if self._stock + new_stock < 20:
            self._stock = self._stock + new_stock
        else:
            messagebox.askyesno("Error!", "You are unable to have a stock grater than 20 items. Please check the number you are trying to stockup by and try again.")

    def _sell_film(self, new_sale):
        if self._stock - new_sale >= 0:
            self._num_sold = self._num_sold + new_sale
            self._stock = self._stock - new_sale
        else:
            messagebox.askyesno("Error!", "You do not have enough of this film in stock. please try again.")

def update_label():
    film_info.set("")
    
    for p in films:
        film_info.set(film_info.get() + p._name + "  $" + str(p._price) + " Stock:" + str(p._stock) + " Number Sold:" + str(p._num_sold) + "\n")

def update_optionmenu():
    global film_menu
    film_menu.children["menu"].delete(0, "end")
    for p in films:
        film_menu.children["menu"].add_command(label=p._name, command=lambda film=p._name: selected_film.set(film))
    selected_film.set("Select a film")

def update_sell_menu():
    global sell_film_menu
    sell_film_menu.children["menu"].delete(0, "end")
    for f in films:
        sell_film_menu.children["menu"].add_command(label=f._name, command=lambda film=f._name: selected_film.set(film))
    selected_film.set("Select a film")

# a new film, update the price and update the stock
def add():
    global film_menu
    Film(new_film.get(), new_price.get(), 0, 0)
    update_label()
    update_optionmenu()
    update_sell_menu()

def edit():
    for f in films:
        if f._name == selected_film.get():
            if edit_price.get() > 0:
                f._update_price(edit_price.get())
            else:
                messagebox.askyesno("Error!", "The price of a film cannot be below $0, If you wish for the film to be free set the price to $0")
    update_label()

def update_stock():
    for f in films:
        if f._name == selected_film.get():
            f._update_stock(edit_stock.get())
    update_label()

def sell_film():
    for f in films:
        if f._name == selected_film.get():
            f._sell_film(sale_num.get())
    update_label()

def delete():
    messege = "Are you sure you want to delete " + selected_film.get()
    if messagebox.askyesno("Warning!", messege):
        for p in films:
            if p._name == selected_film.get():
                films.remove(p)
        update_optionmenu()      
        update_label()

# Show film info when clicked on
def popup():
    top = Toplevel()
    top.title("Popup!")
    name_val = StringVar()
    name_val.set("HELLOOOOO")
    lbl = Label(top, text="asdasdas").grid(row=0)
    for p in films:
        if p._name == selected_film.get():
            name_val.set(p._name)
            print(p._name)
    name_lbl = Label(top, textvariable=name_val, bg="red").grid(row=1)
    destroy_btn = Button(top, text="Close", command=top.destroy).grid(row=2)

# films contains all objects
# film_names contains the names of each film
films = []
film_names = []

Film("Iron Man", 10, 10, 0)
Film("Ant Man", 5, 10, 0)

# -----------------------------
#           VIEWS 
# -----------------------------

# Create the window and give it a title. Set window size to fit the display.
window = Tk()
window.title("RentFlix")
window.geometry('6000x5000')
 
#NoteBook Tabs / Frame Views
tab_control = ttk.Notebook(window)
# Create Frames
admin = ttk.Frame(tab_control)
sell = ttk.Frame(tab_control)
add_film = ttk.Frame(tab_control)
 
# Page Controls & Give labels
tab_control.add(admin, text='Admin')
tab_control.add(sell, text='Sell')
tab_control.add(add_film, text='Add Film')
 


# ----------- ADMIN -----------

# label to display the price list
film_info = StringVar()

film_lbl = Label(admin, textvariable=film_info)
film_lbl.grid(row = 0)

# option menu with all films
selected_film = StringVar()
selected_film.set("Select a film")
film_menu = OptionMenu(admin, selected_film, *film_names)
film_menu.grid(row = 4)

# entry field for editing stock
edit_stock = IntVar()
edit_entry = Entry(admin, textvariable=edit_stock).grid(row=7, column=1)

# button to edit the stock
edit_stock_btn = Button(admin, text="Edit Stock", command=update_stock).grid(row=7, column=2)

# entry field for editing price
edit_price = IntVar()
edit_entry = Entry(admin, textvariable=edit_price).grid(row=4, column=1)

# button to edit the price
edit_btn = Button(admin, text="Edit price", command=edit).grid(row=4, column=2)

# delete button
delete_btn = Button(admin, text="Delete", command=delete).grid(row=5, column=1)


# ----------- Sell -----------
 
# Show Select Menu
selected_film = StringVar()
selected_film.set("Select a film")
sell_film_menu = OptionMenu(sell, selected_film, *film_names)
sell_film_menu.grid(row = 4)

# Number To Sell
sale_num = IntVar()
edit_entry = Entry(sell, textvariable=sale_num).grid(row=8, column=1)

# button to sell
edit_btn = Button(sell, text="Sell Film", command=sell_film).grid(row=8, column=2)


# ----------- Add Film -----------

# entry fields for new film name and price
new_film = StringVar()
new_price = StringVar()
new_film.set("Enter film name")
new_price.set("Price")

film_entry = Entry(add_film, textvariable = new_film).grid(row = 2)
price_entry = Entry(add_film, textvariable = new_price).grid(row = 2, column = 1)

# button to add a new film  object
add_btn = Button(add_film, text="Add new film", command=add).grid(row = 3)

# View / Tab Control
tab_control.pack(expand=1, fill='both')


# ----------- Page Controls -----------

#Update Things
update_label()

# Inetiate the window
window.mainloop()