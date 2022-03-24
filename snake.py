from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = self.init_snake
        self.head = self.snake_body[0]
        self.head.shape("circle")
        self.head.shapesize(1, 1.7)
        self.tail = self.snake_body[-1]

    @property
    def init_snake(self):
        """Create snake body. Returns array of 3 turtles."""
        snake_body = []
        coord = 20
        for i in range(0, 3):
            s = Turtle(shape="square")
            s.color("white")
            s.penup()
            s.setx(coord)
            coord -= 20
            snake_body.append(s)
        return snake_body

    def move_snake(self):
        """Move the snake in the direction it is facing"""
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setpos(self.snake_body[i - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow_snake(self):
        s = Turtle(shape="square")
        s.color("white")
        s.penup()
        s.setpos(self.tail.pos())
        self.snake_body.append(s)

    def check_collision(self):
        collision = False
        for segment in self.snake_body[2:]:
            if self.head.distance(segment) < 5:
                collision = True
        return collision
