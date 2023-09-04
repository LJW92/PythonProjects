from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
word_current = {}


# ------------------------------ Read the csv file ------------------------------#
def next_card():
    global word_current, timer
    window.after_cancel(timer)
    word_current = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(word_text, fill='black', text=f"{word_current['French']}")
    canvas.itemconfig(nation_text, fill='black', text='French')
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(word_text, fill='white', text=f"{word_current['English']}")
    canvas.itemconfig(nation_text, fill='white', text='English')


def is_known():
    global word_current
    to_learn.remove(word_current)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------ Read the csv file ------------------------------#
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
# ------------------------------ UI ------------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
nation_text = canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
