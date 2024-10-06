from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-100,250)
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f" SCORE : {self.score}",font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_score()
    def Game_over(self):
        self.clear()
        self.penup()
        self.goto(-100,0)
        self.write(f"Game Over",font=FONT)
        self.goto(-100,-50)
        self.write(f" SCORE:{self.score}",font=FONT)
        
    
