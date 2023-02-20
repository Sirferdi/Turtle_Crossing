from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.level = 1
        self.write(f"level:{self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

