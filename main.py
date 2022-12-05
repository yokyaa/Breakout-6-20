import turtle
from turtle import Turtle, tracer
from random import choice
import time


class Bars(Turtle):
    colors = ["white", "green", "red", "yellow", "blue", "pink", "purple", "gray", "gold", "brown"]

    def __init__(self, x, y):
        super().__init__()
        self.hit = False
        self.shapesize(1, 2)
        self.shape("square")
        self.color(choice(self.colors))
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=2.5)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -300)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


class Ball(Turtle):
    def __init__(self):
        random_list = [10, -10]
        random_move = choice(random_list)
        super().__init__()

        self.penup()
        self.color("blue")
        self.shape("circle")
        self.x_move = random_move
        self.y_move = 10
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9


class Game:
    tx, ty = -250, 300
    bars = []

    def __init__(self):
        tracer(0)
        self.paddle = Paddle()
        self.ball = Ball()
        for _ in range(5):
            for _ in range(10):
                target = Bars(self.tx, self.ty)
                self.bars.append(target)
                self.tx += 55
            self.ty -= 25
            self.tx = -250
        tracer(1)

    def refresh(self):
        self.ball.move()
        if self.ball.ycor() < -300:
            exit()
            print("y")
        if self.ball.ycor() > 300:
            self.ball.y_bounce()
        if self.ball.ycor() >= 175:
            for bar in self.bars:
                if not bar.hit:
                    if self.ball.distance(bar) < 25:
                        if self.ball.xcor() >= bar.xcor() - 25:
                            if self.ball.xcor() <= bar.xcor() + 25:
                                self.ball.y_bounce()
                                bar.color("black")
                                bar.hit = True
                                break
        if self.ball.xcor() <= -360 or self.ball.xcor() >= 360:
            self.ball.x_bounce()
        if self.ball.ycor() <= self.paddle.ycor() + 25:
            if self.ball.xcor() >= self.paddle.xcor() - 50:
                if self.ball.xcor() <= self.paddle.xcor() + 50:
                    self.ball.y_bounce()


def keys(paddle):
    turtle.onkeypress(paddle.go_left, "Left")
    turtle.onkeypress(paddle.go_right, "Right")


def start():
    turtle.bgcolor(0, 0, 0)
    game = Game()
    keys(game.paddle)
    turtle.listen()

    while 1:
        time.sleep(game.ball.move_speed)
        game.refresh()


start()
turtle.exitonclick()
