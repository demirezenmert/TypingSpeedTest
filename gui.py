from tkinter import *
from tkinter.ttk import *
from main import typing_tester
from time import time


window = Tk()
window.geometry('500x300')
window.title('Typing Speed Tester.')


title_label = Label(window, text='Typing Speed Tester',font=('arial',30))
title_label.pack()

sample_text = 'Today is sunny!'

sample_label = Label(window, text=sample_text, font=('arial',20)).pack()

user_text = StringVar()
user_input = Entry(window, textvariable=user_text)
user_input.pack()


# Start timer 
start_time = time()
# Wait for the user to press the Enter key

user_input.focus_set()
window.bind("<Return>", lambda event: calculate_results(user_input.get(), sample_text, start_time))

def calculate_results(user_input, sample_text, start_time):
    typing_tester(user_input, sample_text, start_time)
    

window.mainloop()