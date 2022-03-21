from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Sneaky Snake")

scoreboard = Scoreboard()

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

food = Food()

game_over = False
while not game_over:
    screen.update()
    snake.move_snake()
    time.sleep(.1)

    # Detect food collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.grow_snake()
        food.rand_pos()

    # Detect collision with tail
    game_over = snake.check_collision()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        game_over = True
    elif snake.head.ycor() >290 or snake.head.ycor() < -290:
        game_over = True

scoreboard.game_over()

screen.exitonclick()
