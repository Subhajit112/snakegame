from turtle import Turtle
from random import randint
from Snake import snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1.0,1.0,1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        foodx= randint(-300,300)
        foody= randint(-300,300)
        self.goto(foodx,foody)

