from turtle import Turtle
import random


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
