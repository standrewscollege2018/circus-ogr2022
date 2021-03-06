####-----------------------####
##---------------------------##
#        RENT FILX            #
#           1.4               # 
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
    
    # Set the films into the array.
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock
        self._num_sold = 0
        films.append(self)
        film_names.append(self._name)

    # Update the price overiding the old one with the new one from the entry feild.
    def update_object_price(self, price):
        self._price = price

    # If the stock total stock will not exceed 20 and is not less than 0 allows the user to add or remove stock
    # if it fails show an error messege 
    def update_object_stock(self, new_stock):
        if self._stock + new_stock <= 20 and self._stock + new_stock >= 0:
            self._stock = self._stock + new_stock
            messagebox.showinfo("Stock Updated", "The films stock has been updated.")
        else:
            messagebox.showinfo("Error!", "You are unable to have a stock grater than 20 items. Please check the number you are trying to stockup by and try again.")

    # Try removing the number wanted to sell from film
    # add the numbered sold to the films total sold
    def update_object_sell(self, new_sale):
        try:
            sale_number = int(new_sale)

            if self._stock - new_sale >= 0 and new_sale > 0:
                number_to_sell = str(new_sale)
                total_sale_price = str(self._price * new_sale)
                check_messege = "Are you sure you want to sell " + number_to_sell + " films for a total of: $" + total_sale_price
                if messagebox.askyesno("Check New Film", check_messege):
                    self._num_sold = self._num_sold + new_sale
                    self._stock = self._stock - new_sale
                    messagebox.showinfo("Film Added", "The sale has been completed.")
                    update_label()
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

# Resets the text variable that hold the conent for the films then loops through the films adding them back.
def update_label():
    film_info.set("")
    for f in films:
        film_info.set(film_info.get() + f._name + "\n" + "Price: $" + str(f._price) + "    Stock: " + str(f._stock) + "    Number Sold: " + str(f._num_sold) + "\n" + "\n")

# Removes the children then adds them back to the option men looping though the list of film_names adding their names as children.
def update_optionmenu():
    global film_menu
    film_menu.children["menu"].delete(0, "end")
    for f in films:
        film_menu.children["menu"].add_command(label=f._name, command=lambda film=f._name: selected_film.set(film))
    selected_film.set("Select A Film")

# a new film, update the price and update the stock
def add():
    global film_menu
    # Check if any films exsits with the same name. If so tell the user that film allready exists.
    if not any(f._name.lower() == new_film.get().lower() for f in films):
        # Try change the input value to an int
        try:
            add_price = int(new_price.get())

            # Check if the entered price is larger than 0, if it is zero then ask the user that they ment to set the price to 0
            if add_price >= 0 and new_film.get():
                if new_price.get() == 0:
                    if messagebox.askyesno("Film price is $0", "Is this correct?"):
                        Film(new_film.get(), new_price.get(), 0)
                        check_messege = "The new film: " + new_film.get() + " has been added with a price of $" + new_price.get()
                        messagebox.showinfo("Film Added", check_messege)
                else:
                    # Confim wether the user wants to add the film.
                    check_messege = "Are you sure you want to add the film: " + new_film.get() + " With a price of: $" + new_price.get()
                    if messagebox.askyesno("Check New Film", check_messege):
                        Film(new_film.get(), new_price.get(), 0)
                        check_messege = "The new film: " + new_film.get() + " has been added with a price of $" + new_price.get()
                        messagebox.showinfo("Film Added", check_messege)
            else:
                messagebox.showinfo("Error", "The films price must be a positive interger e.g. 0 and you must set a film name")
        # If changing the value to an Int errors then ask the user to enter a postive interger
        except ValueError:
            messagebox.showinfo("Error", "The films price must be a positive interger e.g. 0")
        except TypeError:
            messagebox.showinfo("Error", "There was an unknown type error.")
    else:
        check_messege = "The film " + new_film.get() + " Already exists."
        messagebox.showinfo("Duplicate Films", check_messege)
    update_label()
    update_optionmenu()

# Try running the edit funtcion to edit the price
# if they cause an error then show an error messege
def edit():
    if selected_film.get().lower() != "select a film":
        for f in films:
            if f._name == selected_film.get():
                try:
                    # Try turning the entered value into an interger for error checking.
                    update_price = int(edit_price.get())
                    
                    if edit_price.get() >= 0:
                        print_new_price = str(edit_price.get())
                        # Confim wether the user wants to update the price
                        check_messege = "Are you sure you want to change the price of: " + selected_film.get() + " to $" + print_new_price
                        if messagebox.askyesno("Check New Film", check_messege):
                            f.update_object_price(edit_price.get())
                            check_messege = "The price for the film: " + selected_film.get() + " has been updated to $" + print_new_price
                            messagebox.showinfo("Price Updated", check_messege)
                            update_label()
                    else:
                        messagebox.showinfo("Error!", "The price of a film cannot be below $0, If you wish for the film to be free set the price to $0")
                except:
                    messagebox.showinfo("Error", "The films price must be a positive interger e.g. 0")
    else:
        messagebox.showinfo("Error", "You must select a film first.")

# Try running the stockup fucnction getting the selected film form the option menu and the number to add to the stock from the entry feild
# If it fails ask the user to enter a positive interger to stockup by.
def update_stock():
    if selected_film.get().lower() != "select a film":
        try:
            for f in films:
                if f._name == selected_film.get():
                    f.update_object_stock(edit_stock.get())
            update_label()
        except:
            messagebox.showinfo("Error", "The number of films to stock up by must be a positive interger e.g. 0")
    else:
        messagebox.showinfo("Error", "You must select a film first.")

# Try running the function using the number of the selected film to sell to sell a film
# If it fails ask the user to enter a positive interger
def sell_film():
    if selected_film.get().lower() != "select a film":
        try:
                for f in films:
                    if f._name == selected_film.get():
                        f.update_object_sell(sale_num.get())
                update_label()
        except:
            messagebox.showinfo("Error", "The number of films to sell must be an interger e.g. 0")
    else:
        messagebox.showinfo("Error", "You must select a film first.")

# Get the selected film from the drop down menu, loop through all films until we have the one selected and remove it.
# Ask the user if they are sure before removing.
def delete():
    if selected_film.get().lower() != "select a film":
        
        check_messege = "Are you sure you want to remove the film: " + selected_film.get()
        if messagebox.askyesno("Warning!", check_messege):
            for f in films:
                if f._name == selected_film.get():
                    films.remove(f)
            update_optionmenu()      
            update_label()
    else:
        messagebox.showinfo("Error", "You must select a film first.")

# films contains all objects
# film_names contains the names of each film
films = []
film_names = []

Film("Iron Man", 10, 10)
Film("Ant Man", 5, 10)

# -----------------------------
#            VIEW 
# -----------------------------

root = Tk()
root.title("Rent Filx - Version 1.4")
root.geometry('1045x5000')

# # --------- Row One -----------
# photo = PhotoImage(file="banner.png")
# photo = photo.subsample(4)
# photo_lbl = Label(root, image=photo)
# photo_lbl.grid(row = 0, padx=0, pady=0, columnspan=4)

# --------- Row Two -----------
films_title_lbl = Label(root, font=("Roboto 30 bold"), fg="red", text="Films:")
films_title_lbl.grid(row = 2, column=0, padx=0, pady=10, columnspan=2)

# option menu with all films
# this allows the user to select a film saving it into the selected_film variable to sell, restock, edit price or delete.
selected_film = StringVar()
selected_film.set("Select A Film")
film_menu = OptionMenu(root, selected_film, *film_names)
film_menu.grid(row = 2, column=2, columnspan=2)

# -------- Row Three ----------
# label to display the price list
film_info = StringVar()
film_lbl = Label(root, textvariable=film_info)
film_lbl.grid(row = 3, column=0, columnspan=2, rowspan = 6)

# --------- Row Four -----------
# Entry for the number of films the user wishes to sell
# The user can enter and interger here for the number of films they want to sell for the film selected in the option menu.
sale_num = IntVar()
num_sell_entry = Entry(root, textvariable = sale_num).grid(row = 4, column = 2)

# button to sell
# submits the sale_num variable to the sell function
num_sell_bnt = Button(root, text="Sell Film", command = sell_film).grid(row = 4, column = 3)

# --------- Row Five -----------
# Entry feild for the number of films they want to stock up by.
edit_stock = IntVar()
add_stock_entry = Entry(root, textvariable=edit_stock).grid(row = 5, column = 2)

# button to edit the stock
# submits the edit_stock interger variable. to the sell function.
add_stock_btn = Button(root, text="Edit Stock", command = update_stock).grid(row = 5, column = 3)

# --------- Row Six ------------
# Entry feild for the price they want to change the selected feild from the option menu to.
edit_price = IntVar()
edit_entry = Entry(root, textvariable=edit_price).grid(row = 6, column = 2)

# button to edit the price
# submits the edit_price interger variable to the edit function.
edit_btn = Button(root, text="Edit price", command = edit).grid(row = 6, column = 3)

# -------- Row Seven -----------
# delete button
# removed the film slected in the option menu from both the films list and the film_names list.
delete_btn = Button(root, text="Delete", command = delete).grid(row = 7, column = 2, columnspan = 2, pady = (20, 0))

# -------- Row Eight -----------
add_lbl = Label(root, text="Add A Film:", font=("Roboto 20 bold"), fg="red")
add_lbl.grid(row = 8, column=0, padx=0, pady = (60, 10), columnspan=4)

# -------- Row Nine -----------
# entry fields for new film name and price
new_film = StringVar()
new_price = StringVar()
new_film.set("Enter film name")
new_price.set("Price")

film_entry = Entry(root, textvariable = new_film).grid(row = 9, column = 0, columnspan = 2)
price_entry = Entry(root, textvariable = new_price).grid(row = 9, column = 2)

# button to add a new film  object
add_btn = Button(root, text="Add new film", command=add).grid(row = 9, column = 3)

# -----------------------------
#       Page Controls
# -----------------------------

update_label()
root.mainloop()
