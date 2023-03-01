import random
import turtle

from racket import Racket
from turtle import Screen
from score import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(900, 500)
screen.tracer(0)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

right_racket = Racket(400)
right_racket_score = Score(110, 170)
left_racket = Racket(-400)
left_racket_score = Score(-130, 170)
ball = Ball()

x = 0
y = 250

line = turtle.Turtle()

for _ in range(100):
    y -= 10
    line.setpos(x, y)
    line.width(10)
    line.color("white")
    line.hideturtle()

screen.listen()
screen.onkey(right_racket.move_up, key="Up")
screen.onkey(right_racket.move_down, key="Down")
screen.onkey(left_racket.move_up, key="w")
screen.onkey(left_racket.move_down, key="s")


def on_close():
    global its_on
    its_on = False


root.protocol("WM_DELETE_WINDOW", on_close)

its_on = True

while its_on:

    screen.update()
    right_racket.move()
    left_racket.move()
    ball.move()
    ball.bounce()

    if ball.xcor() <= -500:
        right_racket_score.add_score()

    elif ball.xcor() >= 500:
        left_racket_score.add_score()

    for seg in right_racket.racket:
        if seg.distance(ball.xcor(), ball.ycor()) <= 10:
            ball.angle = random.randrange(250, 180, -1)

    for seg in left_racket.racket:
        if seg.distance(ball.xcor(), ball.ycor()) <= 10:
            ball.angle = random.randrange(80, 0, -1)

    if ball.xcor() >= 500 or ball.xcor() <= -500:
        ball.restart_ball()
        ball.move()

    if not its_on:
        break
