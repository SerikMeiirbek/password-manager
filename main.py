from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if not validate_input_fields():
        messagebox.showinfo(message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website_input,
                                   message=f"These are the details are entered: \nEmail:{email_username_input.get()} "
                                           f"\nPassword:{password_entry.get()} \nIs it ok to save?")

    website = website_input.get()
    new_data = {
        website: {
            "email": email_username_input.get(),
            "password": password_entry.get()
        }
    }

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Dumping data to data_file
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Updating old data with new data
                data.update(new_data)
                # Dumping data to data_file
                json.dump(data, data_file, indent=4)
        finally:
            # Clearing input fields
            clear_input_fields()


# -------------------------- Clear input fields -------------------------- #
def clear_input_fields():
    website_input.delete(0, END)
    password_entry.delete(0, END)


# -------------------------- Check input fields -------------------------- #
def validate_input_fields():
    return website_input.get() != "" and email_username_input.get() != "" and password_entry.get() != ""


# -------------------------- Search Websites -------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Datafile found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                                title=website,
                                message=f"Email:  {email}"
                                f"\nPassword:  {password}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"No details for {website_input.get()} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

# Search
search_btn = Button(text="Search", width=12, command=find_password)
search_btn.grid(row=1, column=2)

# Email/Username
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=38)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "password.manager@gmail.com")

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_generator_btn = Button(text="Generate Password", command=generate_password)
password_generator_btn.grid(row=3, column=2)

# Add
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
