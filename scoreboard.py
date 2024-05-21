from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-20,250)
        self.color("white")
        self.score = 0        
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", False, "center", font=("Arial", 20, "normal"))

    def scoring(self):
         self.score +=1
         self.clear()
         self.update_scoreboard()
         
    def gameover(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("white")  
        self.write("GAME OVER!", False, "center", font=("Arial", 25, "normal"))
        
