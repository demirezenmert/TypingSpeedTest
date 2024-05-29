from tkinter import * 
from tkinter.ttk import *

class GAMEOVER:

    def __init__(self) -> None:
        self.gameOverWindow = Toplevel()
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
        
        self.playerScore = 0
        self.highScore = 0
        self.readScores()

        self.highScoreLabel = Label(self.gameOverWindow, text= f'High Score: {self.highScore}')
        self.playerScoreLabel = Label(self.gameOverWindow, text=f'Your Score: {self.playerScore}')
        self.highScoreLabel.grid(row=3, column=0)
        self.playerScoreLabel.grid(row=3, column=2)


        
        self.gameOverWindow.mainloop()
    
    def exit_game(self):
        self.gameOverWindow.destroy()
    
    def readScores(self):
        with open('scores/playerScore', 'r') as f:
            self.playerScore = int(f.read())
        with open('scores/highScore', 'r') as f:
            self.highScore = int(f.read())
        if self.playerScore > self.highScore :
            self.highScore = self.playerScore
        


