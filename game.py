
from tkinter import *
from tkinter.ttk import *
from main import typing_tester
from time import time
from tkinter import messagebox
import random
from gameOver import GAMEOVER
import data





class GAME:

    def __init__(self, level_time, level_words, level) -> None:
        # Windows Setup
        self.level = level
        self.level_time = level_time
        self.level_words = level_words
        self.topWindow = Toplevel()
        self.topWindow.geometry('600x400')
        self.topWindow.config(padx=50,pady=50)
        self.topWindow.title('Typing Speed Tester')
        self.topWindow.resizable(False,False)
        self.timer = Label(self.topWindow, text= f'Time: {level_time}', font=('arial',20,'bold'))
        self.timer.grid(column=1,row=0)
        self.sample_word = Label(self.topWindow, text='', font=('arial',20,'bold'))
        self.sample_word.grid(column=1,row=1,pady=8)
        
        self.start_button = Button(self.topWindow,text="Start", command=self.start_game)
        self.start_button.grid(row=1, column=1)
        self.user_answer = StringVar()
        self.text_entry = Entry(self.topWindow, width=55, textvariable= self.user_answer)
        self.text_entry.grid(row=2, column=1, pady=30)
        self.text_entry.config(state=DISABLED)

        self.exit_button = Button(self.topWindow,text="Exit", command=self.exit_game)
        self.exit_button.grid(row=3, column=1)

        self.score_label = Label(self.topWindow, text= '')
        self.score_label.grid(row=5,column=1, pady=5)

        self.message = Label(self.topWindow, text="Click the START button to start. Type in the word and hit Enter. \n" 
                             f"\t\tYou'll have {level_time} seconds", font=('Courier', 12, 'bold'),
                             wraplength=500)
        self.message.grid(row=4, column=1, pady=30)
        
        self.sample_word_text = random.choice(self.level_words)
        self.score = 0
        self.accuracy = 0
        self.topWindow.mainloop()

    def start_game(self):
        
        print('## DEBUG : Start Game!')

        
        self.start_button.destroy()
        self.message.destroy()
        self.score_label.config(text=f'Your Score: {self.score}')
        self.text_entry.config(state=NORMAL)
        self.counter(self.level_time)
        self.show_text()
        
    def counter(self, count):
        self.timer.config(text=f'Time: {count}')
        self.score_label.config(text=f'Your Score: {self.score}')

        if count > 0:
            self.topWindow.after(1000, self.counter, count-1)
        else: 
            # messagebox.showinfo("Time's Up", "Game Over!")
            self.save_score()
            self.topWindow.destroy()
            gm = GAMEOVER(self.level)
        
    def increase_score(self):
        if self.accuracy > 80 : 
            self.score += 1
        


    
    def exit_game(self):
        self.topWindow.destroy()
    
    def check_answer(self, user_answer, sample, start_time):
        self.accuracy = typing_tester(user_answer, sample, start_time)
        self.increase_score()

        self.show_text()
    def show_text(self):
        self.text_entry.delete(0, 'end')
        self.sample_word_text = random.choice(self.level_words)
        self.sample_word.config(text=self.sample_word_text)
        self.text_entry.focus()
        start_time = time()
        self.topWindow.bind("<Return>", lambda event: self.check_answer(self.text_entry.get(), self.sample_word_text, start_time))

    def save_score(self):
        
        data.update_scores(self.score, self.level)
        
        

