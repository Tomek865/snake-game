from turtle import Turtle
import random

class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.goto(x, y)