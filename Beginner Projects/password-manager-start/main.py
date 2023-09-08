from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    entry_3.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_1.get()
    username = entry_2.get()
    password = entry_3.get()
    new_data = {
        website: {
            'email': username,
            'password': password,
        }
    }
    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)


# ---------------------------- PASSWORD SEARCH------------------------------- #

def search_password():
    website = entry_1.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title='Error', message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_1 = Label(text='Website:')
label_1.grid(column=0, row=1)

label_2 = Label(text='Email/Username:')
label_2.grid(column=0, row=2)

label_3 = Label(text='Password:')
label_3.grid(column=0, row=3)

# Buttons
button_1 = Button(text='Generate Password', command=generate_password)
button_1.grid(column=2, row=3)

button_2 = Button(text='Add',  width=36, command=save_password)
button_2.grid(column=1, row=4, columnspan=2)

button_3 = Button(text='Search', command=search_password, width=13)
button_3.grid(column=2, row=1)

# Enters
entry_1 = Entry(width=21)
entry_1.grid(column=1, row=1)
entry_1.focus()

entry_2 = Entry(width=35)
entry_2.insert(0, string="ljw9282@foxmail.com")
entry_2.grid(column=1, row=2, columnspan=2)

entry_3 = Entry(width=21)
entry_3.grid(column=1, row=3)

window.mainloop()
