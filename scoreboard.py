from turtle import Turtle

POSITION =(0, 280)
ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("Data.txt", mode="r") as r:
            self.high_score = int(r.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.write(arg=f"score = {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(POSITION)
        self.clear()
        self.write(arg=f"score = {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over!", align=ALIGN, font=FONT)

    def increase_score(self):
        self.goto(POSITION)
        self.clear()
        self.score += 1
        self.write(arg=f"score = {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)
