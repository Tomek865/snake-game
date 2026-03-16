from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        try:
            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())
        except:
            self.high_score = 0
        self.color("white")
        self.goto(0, 265)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}",
                   align="center", font=("Courier", 18, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over",align="center",font=("Arial",24,"normal"))
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")