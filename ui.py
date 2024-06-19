THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrainn

class QuizInterface:
    def correct_button_check(self):
        if QuizBrainn(self.correct_answer).answer_checker("True"):
            self.canvas.config(bg="green")
            self.score = self.score + 1
            self.word_label["text"] = f"Score: {self.score}"
        else:
            self.canvas.config(bg="red")
        self.disable_button()
        self.window.after(1000, self.att_word)


    def false_button_check(self):
        if QuizBrainn(self.correct_answer).answer_checker("False"):
            self.canvas.config(bg="green")
            self.score = self.score + 1
            self.word_label["text"] = f"Score: {self.score}"
        else:
            self.canvas.config(bg="red")
        self.disable_button()
        self.window.after(1000, self.att_word)

    def att_word(self):
        if self.number <= len(self.q_list):
            self.enable_buttons()
            self.correct_answer = self.q_list[self.number][1]
            self.word_input = self.q_list[self.number][0]
            self.number += 1
            self.canvas.itemconfigure(self.word, text=f"{self.word_input}")
        else:
            self.word_input = "O GAME ACABOU  :(("
            self.canvas.itemconfigure(self.word, text=f"{self.word_input}")
            self.disable_button()
        self.canvas.config(bg="white")

    def enable_buttons(self):
        self.false_button.config(state="active")
        self.correct_button.config(state="active")
    def disable_button(self):
        self.false_button.config(state="disabled")
        self.correct_button.config(state="disabled")



    def __init__(self,q_list):
        self.q_list = q_list
        self.number = 0
        self.correct_answer = q_list[self.number][1]
        self.word_input = q_list[self.number][0]
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50,pady=50,background=THEME_COLOR)

        self.word_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.word_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=300)
        self.word = self.canvas.create_text(150, 150,text=f"blablabla", font=("Arial",20,"italic"),width=250)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=30)

        self.false_image = PhotoImage(file="images/false.png")
        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, highlightthickness=0, command=self.correct_button_check)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_button_check)
        self.correct_button.grid(row=3,column=0,pady=30)
        self.false_button.grid(row=3,column=1)

        self.att_word()
        self.window.mainloop()

