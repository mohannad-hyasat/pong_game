from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.angle = 160
        self.setheading(self.angle)

    def h_left(self):
        self.angle += 180
        self.setheading(self.angle)

    def h_right(self):
        self.angle -= 180
        self.setheading(self.angle)

    def move(self):
        if self.ycor() > 330:
            if self.angle < 90:
                self.angle += 45
                self.setheading(self.angle)
            else:
                self.angle -= 45
                self.setheading(self.angle)
        elif self.ycor() < -330:
            if self.angle < 270:
                self.angle -= 45
                self.setheading(self.angle)
            else:
                self.angle += 45
                self.setheading(self.angle)

        self.forward(20)