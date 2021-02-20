from turtle import Turtle
import random
ALIGNMENT='center'
Font=("Courier", 24, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color('yellow')
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=Font)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write('thua tan nat ', align=ALIGNMENT, font=Font)