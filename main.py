import time
from turtle import Screen, Turtle, width
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

mooving = True
while mooving:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Food eating and score count
    if snake.head.distance(food) < 15:
        food.newFood()
        snake.extend()
        scoreboard.scoreInc()
    
    #Wall detection
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        mooving= False
        scoreboard.gameOver()

    #Tail detection
    for block in snake.blocks:
        if block == snake.head:
            pass
        elif snake.head.distance(block) < 10:
            mooving= False
            scoreboard.gameOver()


screen.exitonclick()
