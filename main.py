# from tkinter import all classes and constants
from tkinter import *
# import Tkinter messagebox module
from tkinter import messagebox
from random import randint, choice, shuffle
# Pyperclip is a cross-platform Python module for copy and paste clipboard functions
import pyperclip
# import json module
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # list comprehension
    # [new_item for item in list if test]
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # the data that we want to put in json.dump() should go in as a dictionary
    # i.e create a new dictionary (a nested dictionary)
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # make sure all the fields have been entered
    if len(website) > 0 and len(password) > 0:
        # if user confirm a yes to the details entered
        # ask a question, return true if the answer is yes
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
        #                                                    f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:

        # JSON - JavaScriptObjectNotation
        # One of the most popular ways of transferring data
        # Especially when you're transferring data across the internet
        # A JSON is essentially composed of a bunch of nested lists and dictionaries
        # and it has the key and value pair data structure
        # JSON is a format that encodes objects in a string
        # Serialization means to convert an object into that string
        # Deserialization converts string into an object

        try:
            # change the data format from .txt into .json
            # try to read a file called data.json
            with open("data.json", mode="r") as data_file:
                # data.write(f"{website} | {email} | {password}\n")

                # write data to a json file
                # the most important inputs for json.dump() are:
                # the things you want to dump
                # and the file that you want to dump it to
                # we can provide the number of spaces to indent all the JSON data
                # json.dump(new_data, data_file, indent=4)

                # serialize
                # json_data = json.dumps(new_data, indent=4)
                # print(json_data)

                # read a json file
                # deserialize
                # data = json.load(data_file)
                # json.load() method takes a json data and converts it into a Python dictionary
                # i.e we can use json.dump() and json.load() to:
                # serialize and deserialize from json data to Python dictionary
                # it allows us that free interchange of information
                # we change it into json to store it,
                # and then we take it out of storage and turn it into a Python dictionary
                # to easily work with it in our code
                data = json.load(data_file)
                # print(data)
                # print(type(data))
        except FileNotFoundError:
            # if the file is not found and we can't read it, we create a new data.json file
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # we want to update data
            # if we have a new piece of data come in,
            # we want to add to the json file
            # but we don't want to overwrite it nor just append to it (i.e invalid data structure)

            # if it reads the file successfully, we update it with a new entry
            # data is of type dictionary
            # we use the update() method to update that dictionary with some new piece of data
            data.update(new_data)
            # we want to write this data back into the json file, i.e data_file
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
                # the entire json file has now been updated to have two entries
                # the new entry (i.e new_data) is added into the dictionary (i.e data) by the update() method
                # once it updated that data, we told it to save the updated data back into the data_file,
                # and wipe all of the previous data
        finally:
            # No matter if it succeeds or fails
            # delete fields anyway
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        # display an error message
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # check if user input in the website_entry has the same data in json file
    website = website_entry.get()
    try:
        # read the json file
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            # print(data)
            # e.g {'Amazon': {'email': 'name@email.com', 'password': 'N8%I%XD(6f3sn1*f'}}
            # print(type(data))
            # <class 'dict'>
            # print(data[website])
            # e.g {'email': 'name@email.com', 'password': 'N8%I%XD(6f3sn1*f'}
    except FileNotFoundError:
        # display a message to the user that there is no data
        messagebox.showinfo(title="error", message="Sorry there is no data in the file.")
    else:
        if website in data:
            # get hold of the value by the key in dictionary
            email = data[website]["email"]
            password = data[website]["password"]
            # display the account credentials to the user after searching
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # display a message to the user that data cannot be found in the file
            messagebox.showinfo(title="error", message="Sorry the data you requested cannot be found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create a canvas widget
canvas = Canvas(width=200, height=200)

# load an image
logo_image = PhotoImage(file="logo.png")

# create an image on the canvas
canvas.create_image(100, 100, image=logo_image)

# get the canvas to have a layout
canvas.grid(column=1, row=0)

# label widget
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entry widget
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.insert(0, "name@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# button widget
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()