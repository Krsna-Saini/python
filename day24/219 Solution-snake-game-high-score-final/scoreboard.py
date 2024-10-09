from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Use a raw string for the file path to avoid escape sequence issues
        self.file_path = r"D:\pythan\day24\219 Solution-snake-game-high-score-final\data.txt"
        try:
            with open(self.file_path) as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            print("High score file not found. Setting high score to 0.")
            self.high_score = 0
        except ValueError:
            print("Error reading high score. Setting high score to 0.")
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            try:
                with open(self.file_path, mode="w") as data:
                    data.write(f"{self.high_score}")
            except Exception as e:
                print(f"Error writing high score: {e}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
