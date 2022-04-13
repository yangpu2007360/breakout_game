from turtle import Turtle
import random


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, -80)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=("Arial", 30, "normal"))
