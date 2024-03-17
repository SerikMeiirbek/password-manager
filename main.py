from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email/Username
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "password.manager@gmail.com")

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_generator_btn = Button(text="Generate Password")
password_generator_btn.grid(row=3, column=2)

# Add
add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()