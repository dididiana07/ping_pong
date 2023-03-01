from turtle import Turtle
from time import sleep
import random

x = 900
y = 500


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("pink")
        self.penup()
        self.angle = random.randint(0, 370)

    def move(self):
        sleep(0.04)
        self.setheading(self.angle)
        self.forward(10)

    def restart_ball(self):
        self.setpos(0, 0)

    def bounce(self):
        if self.ycor() >= 250 or self.ycor() <= -250:
            self.angle = - self.angle
