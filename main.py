import turtle
from turtle import Screen, Turtle
import easygui

from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import random
import sys
import os

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Breakout!")
screen.tracer(False)

scoreboard = Scoreboard()
paddle = Turtle()
paddle.shape("square")
paddle.color("black")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)
color = ["red", "green", "orange", "blue", "purple"]

count = 0
ball = Ball()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    print("rerun")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def check():
    global game_is_on
    if count >= 2 and count < 4:
        scoreboard.level = 2
        scoreboard.clear()
        scoreboard.write(f"Level: {scoreboard.level}", align="center", font=("Arial", 30, "normal"))
        ball.x_move = 5
        ball.y_move = 5
    elif count > 4 and count < 6:
        scoreboard.level = 3
        scoreboard.clear()
        scoreboard.write(f"Level: {scoreboard.level}", align="center", font=("Arial", 30, "normal"))
        ball.x_move = 7
        ball.y_move = 7
    elif count >= 6:
        turtle.hideturtle()
        turtle.color("deep pink")
        turtle.write("You Won!", move=False, align="center", font=("Arial", 30, "normal"))
        answer = easygui.ynbox('Click Yes to play again', 'Congratulations!')
        if answer:
            print("restart")
            restart_program()

        game_is_on = False


def go_left():
    if paddle.xcor() > -330:
        new_x = paddle.xcor() - 20
        paddle.goto(new_x, paddle.ycor())


def go_right():
    if paddle.xcor() < 319:
        new_x = paddle.xcor() + 20
        paddle.goto(new_x, paddle.ycor())


screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

wall_list = []

for raw in range(0, 3):
    for col in range(0, 7):
        x = -342 + col * 115
        y = 280 - 30 * raw
        wall = Wall()
        random_color = random.choice(color)
        wall.color(random_color)
        wall.speed("fastest")
        wall.goto(x, y)
        wall_list.append(wall)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball.xcor() > 330 or ball.xcor() < -330:
        ball.bounce_x()
    if ball.ycor() < -260:
        turtle.hideturtle()
        turtle.color("deep pink")
        turtle.write("Game Over!", move=False, align="center", font=("Arial", 30, "normal"))
        game_is_on = False
        answer = easygui.ynbox('Click Yes to play again', 'Game Over!')
        if answer:
            print("restart")
            restart_program()
    if ball.distance(paddle) < 100 and ball.ycor() < -250 or ball.ycor() > 300:
        print("bounce Y")
        ball.bounce_y()

    for wall in wall_list:
        if ball.distance(wall) < 50:
            ball.bounce_y()
            wall.goto(900, 900)
            count = count + 1
            print(count)
            check()

screen.exitonclick()
