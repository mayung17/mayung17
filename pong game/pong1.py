
import turtle
import winsound

win = turtle.Screen()
win.title("Pong by @mayung")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# paddle a
paddle_a = turtle.Turtle()  # creating obj of Turtle class importing from turtle module
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle b
paddle_b = turtle.Turtle()  # creating obj of Turtle class importing from turtle module
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# ball
ball = turtle.Turtle()  # creating obj of Turtle class importing from turtle module
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.dx = 0.27
ball.dy = 0.27
ball.penup()
ball.goto(0, 0)

# Scoring system
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A:0          PlayerB:0" ,align="center" ,font=("Courier", 24, "normal"))

# score
score_a = 0
score_b = 0
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Function for second paddle
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    win.update()

    # Moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A:{}          PlayerB:{}".format(score_a ,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {}          PlayerB: {}".format(score_a ,score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)
        ball.dx *= -1
