from turtle import Turtle


class Racket:

    def __init__(self, x_pos):
        self.racket = []
        self.y_position = 20
        for _ in range(4):
            self.y_position += 20
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(x_pos)
            new_segment.sety(self.y_position)
            self.racket.append(new_segment)
        self.head = self.racket[0]

    def move(self):
        y_pos = 0
        for seg in self.racket[1:]:
            y_pos += 20
            x = self.head.xcor()
            y = self.head.ycor() + y_pos
            seg.goto(x, y)

    def move_up(self):
        self.head.setheading(90)
        self.head.forward(10)

    def move_down(self):
        self.head.setheading(270)
        self.head.forward(10)
