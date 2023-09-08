from tkinter import *


def button_clicked():
    given = float(user_input_1.get())
    result = round(given * 1.609344, 2)
    label_3['text'] = str(result)


window = Tk()
window.title("Mile to Km converter")
window.config(padx=25, pady=25)


label_1 = Label(text=' Miles', font=('Arial', 18))
label_2 = Label(text='is equal to', font=('Arial', 18))
label_3 = Label(text='0', font=('Arial', 18))
label_4 = Label(text='Km', font=('Arial', 18))

label_1.grid(column=2, row=0)
label_2.grid(column=0, row=1)
label_3.grid(column=1, row=1)
label_4.grid(column=2, row=1)

button_1 = Button(text='Calculate', command=button_clicked)
button_1.grid(column=1, row=2)

user_input_1 = Entry(width=15)
user_input_1.grid(column=1, row=0)



window.mainloop()
