from turtle import Turtle


class Score(Turtle):
    def __init__(self, racket: str, x_pos, y_pos):
        super().__init__()
        self.racket = racket
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(x_pos, y_pos)
        self.color("white")
        self.write(f"{racket} player: {self.score}", font=("Helvetica", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.racket} player: {self.score}", font=("Helvetica", 20, "normal"))





