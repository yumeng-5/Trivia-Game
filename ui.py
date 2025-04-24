from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question = self.canvas.create_text(150, 125, width=280, text="question", font=("Arial","16","italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font="10")
        self.score.grid(column=1, row=0)

        wrong_img = PhotoImage(file="./images/false.png")
        right_img = PhotoImage(file="./images/true.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.is_false)
        self.wrong_button.grid(column=1, row=2)
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.is_true)
        self.right_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
