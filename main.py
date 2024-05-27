from turtle import Turtle, Screen
import time
from scoreboard import Score
from snake_feature import snake
from food import Food

    
    
screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(1)
score= Score()
Snake= snake()
food= Food()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")


game= True
while game:
    screen.update()
    time.sleep(0.001)
    Snake.forward_movement()

    if Snake.head.distance(food) < 15:
        score.scoring()
        food.refresh()
        Snake.extend()

    if Snake.head.xcor() > 280 or Snake.head.xcor()< -280 or Snake.head.ycor()> 280 or Snake.head.ycor() <-280:
        score.gameover()
        game=False
    
    for i in Snake.newsegment[1:]:
       if Snake.head.distance(i) <10:
            game= False
            score.gameover()

screen.exitonclick()
