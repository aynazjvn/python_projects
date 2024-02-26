from multiprocessing import connection
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
import mysql.connector
from mysql.connector import errorcode

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    password = password_entry.get()
    web = web_entry.get()
    new_data = {
        f"{web}":
            {"email": email,
             "password": password}
    }

    if len(password) == 0 or len(email) == 0 or len(web) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fileds empty!")

    else:
        try:
            cnx = mysql.connector.connect(user='root', password='@',
                                          host='localhost',
                                          database='mydatabase')
            cursor = cnx.cursor()
            sql_code = '''CREATE TABLE Password(
               id INT AUTO_INCREMENT
               Website_name CHAR(20) NOT NULL,
               Email CHAR(20),
               Password INT,
            )'''
            query = "INSERT INTO Password(Website_name,Email,Password) " \
                    "VALUES(%s,%s,%s)"
            records_to_insert = [(web, email, password)]

            cursor.execute(sql_code)
            cursor.executemany(query, records_to_insert)
            cursor.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File does not found")

    else:
        if website in data:
            web = data[website]
            email = web["email"]
            password = web["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email : {email}\n Password: {password}")

        else:
            messagebox.showerror(title="Error", message=f"No details for {website} does not exist")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
background_photo = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=background_photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)

password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)

email_entry = Entry(width=33)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "jvaynaz@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)
window.mainloop()
