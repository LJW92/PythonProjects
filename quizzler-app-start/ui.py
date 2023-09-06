from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quizz_text = self.canvas.create_text(150,
                                                  125,
                                                  width=280,
                                                  text='quizz',
                                                  font=('Ariel', 20, 'italic'),
                                                  fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_check)
        self.false_button.grid(column=1, row=2)

        self.score = 0
        self.score_label = Label(text=f'Score:{self.score}')
        self.score_label.config(bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score:{self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quizz_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quizz_text, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_check(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_check(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
