from turtle import Turtle


class Paddle:

    def __init__(self, x):
        self.paddle = []
        y=40
        for n in range(4):
            y -= 20
            seg = Turtle()
            seg.penup()
            seg.color("white")
            seg.shape("square")
            seg.goto(x=x, y=y)
            seg.setheading(90)
            seg.speed(0)
            self.paddle.append(seg)
        self.head = self.paddle[0]
        self.tail = self.paddle[3]

    def move(self):
        for seg in self.paddle:
            seg.forward(20)
        if self.tail.ycor() < -330:
            self.up()
        elif self.head.ycor() > 330:
            self.down()

    def up(self):
        for seg in self.paddle:
            seg.setheading(90)

    def down(self):
        for seg in self.paddle:
            seg.setheading(270)
