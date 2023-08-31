from tkinter import *


def button_clicked():
    my_label['text'] = user_input.get()


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)
# Label

my_label = Label(text='I am a label', font=('Arial', 24))
# Update the text
my_label['text'] = 'New Text'
# my_label.config(text='New Text')
my_label.grid(column=0, row=0)

# Button


button_1 = Button(text='Click', command=button_clicked)
button_2 = Button(text='Click', command=button_clicked)
button_1.grid(column=1, row=1)
button_2.grid(column=2, row=0)
# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
