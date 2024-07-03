from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor()
        new_y += 20
        self.goto(new_x, new_y)

    def move_down(self):
        new_x = self.xcor()
        new_y = self.ycor()
        new_y -= 20
        self.goto(new_x, new_y)
