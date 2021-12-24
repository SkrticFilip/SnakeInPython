from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Arial",20,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updateScore

    def updateScore(self):
        self.write(f"score: {self.score}", align=ALIGHMENT, font=(FONT))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGHMENT, font= FONT)

    def scoreInc(self):
        self.score += 1
        self.clear()
        self.updateScore()
        