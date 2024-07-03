from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 75, "normal")
# Inheritance of attributes and methods from the superclass 'Turtle' to the subclass 'Scoreboard'


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
