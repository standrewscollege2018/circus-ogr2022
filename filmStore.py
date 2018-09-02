####-----------------------####
##---------------------------##
#        RENT FILX            #
#           1.3               # 
#      OLIVER G-J 2018        #
##---------------------------##
####-----------------------####


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
        if self._stock + new_stock < 20 and self._stock + new_stock >= 0:
            self._stock = self._stock + new_stock
        else:
            messagebox.showinfo("Error!", "You are unable to have a stock grater than 20 items. Please check the number you are trying to stockup by and try again.")


    def _sell_film(self, new_sale):
        try:
            sale_number = int(new_sale)

            if self._stock - new_sale >= 0 and new_sale > 0:
                number_to_sell = str(new_sale)
                total_sale_price = str(self._price * new_sale)
                check_messege = "Are you sure you want to sell " + number_to_sell + " films for a total of: $" + total_sale_price
                if messagebox.askyesno("Check New Film", check_messege):
                    self._num_sold = self._num_sold + new_sale
                    self._stock = self._stock - new_sale
            else:
                if self._stock - new_sale < 0:
                    error_messege = "You do not have enough of this film in stock."
                elif new_sale < 0:
                    error_messege = "You cannont sell a negitive number of films."
                else:
                    error_messege = "An unknown error occoured, Please try again."
                messagebox.showinfo("Error!", error_messege)
        except ValueError:
            messagebox.showinfo("Error", "The number of films to sell must be a positive interger e.g. 0")

def update_label():
    film_info.set("")
    for f in films:
        film_info.set(film_info.get() + f._name + "  $" + str(f._price) + " Stock:" + str(f._stock) + " Number Sold:" + str(f._num_sold) + "\n")

def update_optionmenu():
    global film_menu
    film_menu.children["menu"].delete(0, "end")
    for f in films:
        film_menu.children["menu"].add_command(label=p._name, command=lambda film=f._name: selected_film.set(film))
    selected_film.set("Select a film")

# a new film, update the price and update the stock
def add():
    global film_menu
    # Check if any films exsits with the same name. If so tell the user that film allready exists.
    if not any(f._name == new_film.get() for f in films):
        # Try change the input value to an int
        try:
            add_price = int(new_price.get())

            # Check if the entered price is larger than 0, if it is zero then ask the user that they ment to set the price to 0
            if add_price >= 0 and new_film.get():
                if new_price.get() == 0:
                    if messagebox.askyesno("Film price is $0", "Is this correct?"):
                        Film(new_film.get(), new_price.get(), 0, 0)
                else:
                    # Confim wether the user wants to add the film.
                    check_messege = "Are you sure you want to add the film: " + new_film.get() + " With a price of: $" + new_price.get()
                    if messagebox.askyesno("Check New Film", check_messege):
                        Film(new_film.get(), new_price.get(), 0, 0)
            else:
                messagebox.showinfo("Error", "The films price must be a positive interger e.g. 0 and you must set a film name")
        # If changing the value to an Int errors then ask the user to enter a postive interger
        except ValueError:
            messagebox.showinfo("Error", "The films price must be a positive interger e.g. 0")
    else:
        check_messege = "The film " + new_film.get() + " Already exists."
        messagebox.showinfo("Duplicate Films", check_messege)
    update_label()
    update_optionmenu()

def edit():
    for f in films:
        if f._name == selected_film.get():
            if edit_price.get() >= 0:
                print_new_price = str(edit_price.get())
                # Confim wether the user wants to update the price
                check_messege = "Are you sure you want to change the price of: " + selected_film.get() + " to $" + print_new_price
                if messagebox.askyesno("Check New Film", check_messege):
                    f._update_price(edit_price.get())
            else:
                messagebox.showinfo("Error!", "The price of a film cannot be below $0, If you wish for the film to be free set the price to $0")
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
    check_messege = "Are you sure you want to remove the film: " + selected_film.get()
    if messagebox.askyesno("Warning!", check_messege):
        for f in films:
            if f._name == selected_film.get():
                films.remove(p)
        update_optionmenu()      
        update_label()

# films contains all objects
# film_names contains the names of each film
films = []
film_names = []

Film("Iron Man", 10, 10, 0)
Film("Ant Man", 5, 10, 0)

# -----------------------------
#            VIEW 
# -----------------------------

root = Tk()
root.title("Add film")
root.geometry('400x400')

# label to display the price list
film_info = StringVar()

film_lbl = Label(root, textvariable=film_info)
film_lbl.grid(row = 0)

# option menu with all films
selected_film = StringVar()
selected_film.set("Select a film")
film_menu = OptionMenu(root, selected_film, *film_names)
film_menu.grid(row = 4)

# entry field for editing price
edit_price = IntVar()
edit_entry = Entry(root, textvariable=edit_price).grid(row=4, column=1)

# button to edit the price
edit_btn = Button(root, text="Edit price", command=edit).grid(row=4, column=2)

# entry field for editing stock
edit_stock = IntVar()
edit_entry = Entry(root, textvariable=edit_stock).grid(row=7, column=1)

# button to edit the stock
edit_btn = Button(root, text="Edit Stock", command=update_stock).grid(row=7, column=2)

# Number To Sell
sale_num = IntVar()
edit_entry = Entry(root, textvariable=sale_num).grid(row=8, column=1)

# button to sell
edit_btn = Button(root, text="Sell Film", command=sell_film).grid(row=8, column=2)

# delete button
delete_btn = Button(root, text="Delete", command=delete).grid(row=5, column=1)

# entry fields for new film name and price
new_film = StringVar()
new_price = StringVar()
new_film.set("Enter film name")
new_price.set("Price")

film_entry = Entry(root, textvariable = new_film).grid(row = 2)
price_entry = Entry(root, textvariable = new_price).grid(row = 2, column = 1)

# button to add a new film  object
add_btn = Button(root, text="Add new film", command=add).grid(row = 3)


# -----------------------------
#       Page Controls
# -----------------------------

update_label()
root.mainloop()