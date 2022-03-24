from turtle import Turtle
FONT = "courier"
PATH = "high_score.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.penup()
        self.ht()
        self.reset()

    # Clear old score and display new score
    def display_score(self):
        self.clear()
        self.setpos(0, 260)
        self.color("white")
        score_str = f"Score: {self.score} High score: {self.high_score}"
        self.write(score_str, True, align="center", font=(FONT, 18, "bold"))

    # Increase and display score
    def increase_score(self):
        self.score += 1
        self.display_score()

    # Get high score from file
    def get_high_score(self):
        with open(PATH, 'r') as f:
            high_score = f.readline()
        return high_score

    # Set new high score and write to file
    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open(PATH, 'w') as f:
            f.write(str(self.high_score))

    # Reset screen
    def reset(self):
        self.set_high_score()
        self.display_score()

    # Display goodbye message
    def game_over(self):
        self.setpos(0, 0)
        self.write("Goodbye.", True, align="center", font=(FONT, 18, "bold"))

    # Display instructions
    def new_game(self):
        self.setpos(0, 0)
        self.color("white")
        message = "Welcome to snake.\nControl with arrows.\nPress 'space' to exit."
        self.write(message, True, align="center", font=(FONT, 18, "bold"))
