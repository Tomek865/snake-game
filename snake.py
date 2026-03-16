from turtle import Turtle

class Snake:
    def __init__(self):
        self.direction_locked = None
        self.pos = [0, 0]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        start_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in start_positions:
            self.add_segment(pos)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.segments.append(segment)

    def add_next_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            for seq_num in range(len(self.segments) - 1, 0, -1):
                x = self.segments[seq_num - 1].xcor()
                y = self.segments[seq_num - 1].ycor()
                self.segments[seq_num].goto(x, y)
            self.segments[0].forward(20)
            self.direction_locked = False

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