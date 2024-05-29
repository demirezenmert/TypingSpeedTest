from tkinter import * 
from tkinter.ttk import *
HIGHSCORE = 0
PLAYERSCORE = 0 
class GAMEOVER:

    def __init__(self) -> None:
        self.gameOverWindow = Tk()
        self.gameOverWindow.geometry('600x400')
        self.gameOverWindow.config(padx=50,pady=50)
        self.gameOverWindow.title('GAME OVER')
        self.gameOverWindow.resizable(False,False)
        
        self.canvas = Canvas(self.gameOverWindow)
        self.canvas.grid(column=1,row=0,columnspan=2)
        
        
        fileName = PhotoImage(file='pics/gameOver.png')
        self.canvas.create_image(100,100, image=fileName)
        
        
        
        self.exit_button = Button(self.gameOverWindow,text="Exit", command=self.exit_game)
        self.exit_button.grid(row=2, column=1, padx=100)
        
        self.highScoreLabel = Label(self.gameOverWindow, text='High Score: 0')
        self.playerScoreLabel = Label(self.gameOverWindow, text='Your Score: 0')
        self.highScoreLabel.grid(row=3, column=0)
        self.playerScoreLabel.grid(row=3, column=2)




        self.gameOverWindow.mainloop()
    
    def exit_game(self):
        self.gameOverWindow.destroy()
    

game = GAMEOVER()