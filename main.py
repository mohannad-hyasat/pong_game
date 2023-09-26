import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=1200)
screen.tracer(0)

midline = []
y = 340
for n in range(18):
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    segment.shapesize(stretch_wid=1.5, stretch_len=0.25)
    segment.goto(x=0, y=y)
    y -= 40
    midline.append(segment)


player = Paddle(-570)
computer = Paddle(560)
scoreBoard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(computer.up, "w")
screen.onkey(computer.down, "s")



gameOn = True


def leave():
    global gameOn
    gameOn = False


screen.onkey(leave, "space")

while gameOn:
    player.move()
    computer.move()
    ball.move()

    for seg in player.paddle:
        if ball.distance(seg) < 20:
            ball.h_right()
    for seg in computer.paddle:
        if ball.distance(seg) < 20:
            ball.h_left()

    if ball.xcor() > 600:
        scoreBoard.r_point()
        ball.goto(0, 0)
        ball.setheading(random.randint(-45, 45))
    elif ball.xcor() < -600:
        scoreBoard.l_point()
        ball.goto(0, 0)
        ball.setheading(random.randint(135, 225))



    time.sleep(0.05)
    screen.update()










screen.exitonclick()
