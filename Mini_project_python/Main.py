import logging
from tkinter import Tk, Label, Button, StringVar, messagebox, Frame, Radiobutton, OptionMenu
from question_bank import easy_question, hard_question, options, answers
from random import shuffle


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Knowledge Quiz")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f8ff")  # Set background color

        self.ques_count = 1
        self.score = 0
        self.current_question = None
        self.correct_answer = None
        self.selected_category = StringVar(value="Select Category")

        # Initial Category Selection Interface
        self.category_frame = Frame(root, bg="#f0f8ff")
        self.category_frame.pack(pady=20)

        self.category_label = Label(self.category_frame, text="Choose a Category:", font=("Arial", 14), bg="#f0f8ff")
        self.category_label.pack(pady=10)

        self.category_menu = OptionMenu(self.category_frame, self.selected_category, "Current Affairs", "General Knowledge", "Technology", "Programming")
        self.category_menu.config(font=("Arial", 12), bg="#add8e6")
        self.category_menu.pack(pady=10)

        self.start_button = Button(self.category_frame, text="Start Quiz", command=self.start_quiz, font=("Arial", 14), bg="#90ee90")
        self.start_button.pack(pady=10)

        # Quiz Interface (Initially Hidden)
        self.quiz_frame = Frame(root, bg="#f0f8ff")
        self.question_label = Label(self.quiz_frame, text="", font=("Arial", 16), wraplength=400, bg="#f0f8ff")
        self.question_label.pack(pady=20)

        self.options_var = StringVar()
        self.options_var.set(None)

        self.options_frame = Frame(self.quiz_frame, bg="#f0f8ff")
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = Radiobutton(self.options_frame, text="", variable=self.options_var, value=i, font=("Arial", 12), bg="#f0f8ff", anchor="w")
            btn.pack(anchor="w", pady=2)
            self.option_buttons.append(btn)

        # Submit and Next buttons in the same row
        self.button_frame = Frame(self.quiz_frame, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        self.submit_button = Button(self.button_frame, text="Submit Answer", command=self.check_answer, font=("Arial", 14), bg="#add8e6")
        self.submit_button.grid(row=0, column=0, padx=5)

        self.next_button = Button(self.button_frame, text="Next Question", command=self.next_question, font=("Arial", 14), bg="#90ee90")
        self.next_button.grid(row=0, column=1, padx=5)

        self.quit_button = Button(self.quiz_frame, text="Quit Game", command=self.quit_game, font=("Arial", 14), bg="#ff6961")
        self.quit_button.pack(pady=10)

        self.score_label = Label(self.quiz_frame, text="Score: 0", font=("Arial", 14), bg="#f0f8ff")
        self.score_label.pack(pady=10)

        self.category_questions = []
        logging.info("QuizApp initialized.")

    def start_quiz(self):
        category = self.selected_category.get()
        if category == "Select Category":
            messagebox.showerror("Error", "Please select a category to start the quiz.")
            return

        if category == "Current Affairs":
            self.category_questions = list(range(1, 6)) + list(range(21, 26))
        elif category == "General Knowledge":
            self.category_questions = list(range(6, 11)) + list(range(26, 31))
        elif category == "Technology":
            self.category_questions = list(range(11, 16)) + list(range(31, 36))
        elif category == "Programming":
            self.category_questions = list(range(16, 21)) + list(range(36, 41))

        shuffle(self.category_questions)
        self.ques_count = 1
        self.score = 0

        # Hide category selection and show quiz interface
        self.category_frame.pack_forget()
        self.quiz_frame.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.ques_count > 10 or not self.category_questions:
            self.end_quiz()
            return

        question_num = self.category_questions.pop(0)
        self.current_question = easy_question(question_num) if question_num <= 20 else hard_question(question_num)
        self.correct_answer = answers(question_num)
        options_list = options(question_num)

        logging.info(f"Question {self.ques_count}: {self.current_question}")
        self.question_label.config(text=f"Question {self.ques_count}: {self.current_question}")

        shuffle(options_list)  # Shuffle options to randomize their order
        for i, option in enumerate(options_list):
            self.option_buttons[i].config(text=option, value=option)

        self.options_var.set(None)
        self.ques_count += 1

    def check_answer(self):
        user_answer = self.options_var.get()
        if user_answer == self.correct_answer:
            self.score += 1
            logging.info(f"Correct Answer! Current Score: {self.score}")
            messagebox.showinfo("Correct!", f"Correct Answer! Your Score: {self.score}")
        else:
            logging.warning(f"Wrong Answer! Correct Answer: {self.correct_answer}. Current Score: {self.score}")
            messagebox.showerror("Wrong!", f"Wrong Answer! Correct Answer: {self.correct_answer}. Your Score: {self.score}")
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

    def end_quiz(self):
        logging.info(f"Quiz ended. Final Score: {self.score}")
        if self.score == 10:
            messagebox.showinfo("Congratulations!", "You have answered all 10 questions correctly!")
        else:
            messagebox.showinfo("Quiz Over", f"Your final score: {self.score}")
        self.root.quit()

    def quit_game(self):
        logging.info("User chose to quit the game.")
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            self.root.quit()


if __name__ == "__main__":
    logging.info("Starting the Quiz Application.")
    root = Tk()
    app = QuizApp(root)
    root.mainloop()
    logging.info("Quiz Application closed.")