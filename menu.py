from tkinter import *
from tkinter.ttk import *
from easy import EASY

class MENU:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.config(padx=100,pady=50)
        self.window.title('Typing Speed Tester')
        self.window.resizable(False,False)
        

        Label(self.window, text='Welcome!', font=('arial',50,'bold')).grid(column=2,row=1,pady=8)
        Label(self.window, text='Select Level', font=('arial',20)).grid(column=2,row=2,pady=70)

        easy_button = Button(text="Easy", command=self.easy_window)
        easy_button.grid(row=3, column=1)
        
        medium_button = Button(text="Medium", command=self.easy_window)
        medium_button.grid(row=3, column=2)
        
        hard_button = Button(text="Hard", command=self.easy_window)
        hard_button.grid(row=3, column=3)



        self.window.mainloop()

    def easy_window(self):
        easy = EASY()

menu = MENU()