import random
from tkinter import Tk
import tkinter as tk
import time

sentensers = [
    "The quick brown fox jumps over the lazy dog, but the dog was too lazy to react.",
    "She sells seashells by the seashore while the waves gently caress the sandy beach.",
    "In a galaxy far, far away, a battle between good and evil rages on, and the fate of the universe hangs in the balance.",
    "Life is like a box of chocolates; you never know what you're gonna get, and that's what makes it so exciting.",
    "To be or not to be, that is the question that has puzzled philosophers and thinkers for centuries.",
    "Time flies when you're having fun, and before you know it, the day is over.",
    "The sun sets in the west, casting a warm and soothing light across the horizon.",
    "Where there's a will, there's a way, and determination can overcome any obstacle.",
    "The early bird catches the worm, and early risers often have a head start in life.",
    "The pen is mightier than the sword, as the power of words can change the course of history.",
    "Actions speak louder than words, and one's deeds reveal their true character.",
    "Beauty is in the eye of the beholder, and what's attractive to one person may not be to another.",
    "Rome wasn't built in a day, and great achievements take time and effort.",
    "A watched pot never boils, but patience is a virtue in the kitchen.",
    "Every cloud has a silver lining, and even in difficult times, there's a glimmer of hope.",
    "When in Rome, do as the Romans do, and adapt to the local customs and culture.",
    "The proof of the pudding is in the eating, and results matter more than promises.",
    "Necessity is the mother of invention, and creative solutions often arise from needs.",
    "You can't have your cake and eat it too, as choices come with consequences.",
    "When the going gets tough, the tough get going, and resilience is the key to overcoming challenges."
]
class typingSpeedApp():
    def __init__(self,app):
        self.app = app
        self.app.title("Typing Speed Test")
        # self.app.geometry("400x200")
        self.text_to_type = 'raveen dilsanka pitawala'
        self.typing_started = False
        self.high_sore = 0
        self.create_wigects()

    def create_wigects(self):

        self.instruction_label = tk.Label(self.app, text="Type the following text as quickly as possible:")
        self.instruction_label.grid(row=0, column=3)

        self.display_text = tk.Label(self.app, text=self.text_to_type, wraplength=400)
        self.display_text.grid(row=1, column=3)

        self.text_width = 30
        self.entry = tk.Text(self.app, width=self.text_width, height=1)
        self.entry.bind("<Key>", self.start_typing)
        self.entry.grid(row=2, column=3)

        self.result_label = tk.Label(self.app, text=f"Typing Speed: 0.00 WPM" ,width=22)
        self.result_label.grid(row=4, column=2)

        self.high_sore_label = tk.Label(self.app, text="High score: 0.00 WPM", width=22)
        self.high_sore_label.grid(row=4, column=4)

        self.emptyLable1 = tk.Label(self.app, text="     ")
        self.emptyLable1.grid(row=5, column=1)
        self.emptyLable2 = tk.Label(self.app, text="     ")
        self.emptyLable2.grid(row=5, column=5)

        self.button = tk.Button(self.app, text="reset", command=self.reset)
        self.button.grid(row=5, column=2)

        self.button = tk.Button(self.app, text="Exit", command=self.app.destroy)
        self.button.grid(row=5, column=4)

    def reset(self):
        self.text_to_type = random.choice(sentensers)
        self.result_label.config(text=f"Typing Speed: 0.00 WPM")
        self.display_text.config(text=self.text_to_type,height=len(self.text_to_type)//30)
        self.entry.config(state='normal')
        self.entry.delete("1.0", "end-1c")


    def start_typing(self, event):
        if self.entry.cget("state") != "disabled":

            if not self.typing_started:
                self.typing_started = True
                self.start_time = time.time()

            user_input = self.entry.get("1.0", "end-1c")

            self.entry.config(height=(len(user_input)// self.text_width) + 1)

            if user_input != self.text_to_type:
                if user_input == self.text_to_type[:len(user_input)]:
                    # self.typing_started = False
                    elapsed_time = time.time() - self.start_time
                    words_typed = len(user_input)
                    try:
                        typing_speed = words_typed / (elapsed_time / 60)
                    except:
                        typing_speed = 0
                    self.result_label.config(text=f"Typing Speed: {typing_speed:.2f} WPM")
                else:
                    self.result_label.config(text=f"wrong")
            else:
                elapsed_time = time.time() - self.start_time
                words_typed = len(self.text_to_type)
                typing_speed = words_typed / (elapsed_time / 60)
                self.result_label.config(text=f"Typing Speed: {typing_speed:.2f} WPM")
                if typing_speed > self.high_sore:
                    self.high_sore = typing_speed
                    self.high_sore_label.config(text=f"High score: {self.high_sore:.2f} WPM")
                self.entry.config(state="disabled")


if __name__ == '__main__':
    root = Tk()
    app = typingSpeedApp(root)
    root.mainloop()