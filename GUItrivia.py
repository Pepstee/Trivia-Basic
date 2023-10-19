import tkinter as tk
from tkinter import messagebox
import random

class TriviaGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia Game")

        self.score = 0
        self.num_questions = 5
        self.current_question, self.correct_answer = self.get_random_question()

        self.question_label = tk.Label(master, text=self.current_question)
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def get_random_question(self):
        questions = {
            "What is the capital of France?": "Paris",
            "Which planet is known as the Red Planet?": "Mars",
            "What is the largest mammal in the world?": "Blue Whale",
            "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
            "What is the square root of 64?": "8",
        }
        question, answer = random.choice(list(questions.items()))
        return question, answer

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.correct_answer.lower():
            messagebox.showinfo("Correct!", "You got it right!")
            self.score += 1
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {self.correct_answer}.")

        self.num_questions -= 1
        if self.num_questions > 0:
            self.current_question, self.correct_answer = self.get_random_question()
            self.question_label.config(text=self.current_question)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Game Over", f"Your final score is {self.score}/{self.num_questions}.")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaGameGUI(root)
    root.mainloop()
