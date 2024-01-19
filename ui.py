from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizIterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title = "Quizeer"
        self.canvas = Canvas(width=80, height=52)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=200, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            font=("Ariel", 12, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.image_true = PhotoImage(file="images/true.png")
        self.image_false = PhotoImage(file="images/false.png")
        self.button_right = Button(image=self.image_true, highlightthickness=0, command=self.answer_true)
        self.button_right.grid(row=2, column=0)
        self.button_wrong = Button(image=self.image_false, highlightthickness=0, command=self.answer_false)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

