from turtle import Turtle

class Snake:
    def __init__(self):
        self.pos = [0, 0]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_segment(i)

    def add_segment(self,position):
            segment = Turtle(shape="square")
            segment.up()
            segment.setpos(self.pos[0], self.pos[1])
            segment.color("white")
            self.segments.append(segment)
            self.pos[0] -= 20

    def add_next_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for seq_num in range(len(self.segments) - 1, 0, -1):
                x = self.segments[seq_num - 1].xcor()
                y = self.segments[seq_num - 1].ycor()
                self.segments[seq_num].goto(x, y)
            self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)