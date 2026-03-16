from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.pensize(5)
        self.speed("fastest")

    def draw_rect(self):
        self.goto(-290,-290)
        self.setheading(0)
        self.pendown()

        for _ in range(4):
            self.forward(580)
            self.left(90)

        self.penup()
