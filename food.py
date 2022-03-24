from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5)
        self.rand_pos()

    def rand_pos(self):
        rand_x = random.randrange(-280, 280, 40)
        rand_y = random.randrange(-280, 280, 40)
        self.setpos(rand_x, rand_y)