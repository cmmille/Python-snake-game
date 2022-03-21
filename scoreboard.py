from turtle import Turtle
FONT = "courier"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.display_score()

    def display_score(self):
        self.clear()
        self.setpos(0, 260)
        score_str = f"Score: {self.score}"
        self.write(score_str, True, align="center", font=(FONT, 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.setpos(0, 0)
        self.color("red")
        self.write("Game over.", True, align="center", font=(FONT, 18, "bold"))
