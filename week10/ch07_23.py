# 이하 코드 작성

import turtle
import time

t = turtle.Turtle()
t.shape("turtle")

for i in range(1, 11):
    t.fillcolor('#%02d%02d%02d' % (100-i, 50-i*2, 25-i*2))
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.up()
    t.goto(i*40, 0)
    t.down()

time.sleep(3)
