from time import sleep
from turtle import Turtle


t = Turtle()
t.shape("turtle")

t.up()
t.goto(-100, 0)
t.down()

t.circle(100)

t.up()
t.goto(90, 0)
t.down()

t.circle(100)

t.up()
t.goto(180, 0)
t.down()

t.circle(100)

t.up()
t.goto(135, -100)
t.down()

t.circle(100)

t.up()
t.goto(225, -100)
t.down()

t.circle(100)


sleep(10)
