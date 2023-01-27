from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
              'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['`', '~', '!', '@', '#', '$',
              '%', '^', '&', '*', '(', ')', '+', '=']

    nr_letter = random.randint(8, 10)
    nr_number = random.randint(2, 4)
    nr_symbol = random.randint(2, 4)

    password_letter = [random.choice(letter) for _ in range(nr_letter)]
    password_number = [random.choice(number) for _ in range(nr_number)]
    password_symbol = [random.choice(symbol) for _ in range(nr_symbol)]

    password_list = password_letter+password_number+password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="website and password sectionn can't be empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are th edetails entered:\nWebsite: {website}\nPassword:{password}\nIs it okey to save ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=180, width=180)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(90, 90, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "subhransh.sr@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
