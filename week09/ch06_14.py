import time
import turtle
b = turtle.Turtle()
b.shape("turtle")

b.fillcolor('#F0F8FF')
b.begin_fill()
b.circle(50)
b.end_fill()

b.up()
b.goto(90, 0)
b.down()

b.fillcolor('#7FFFD4')
b.begin_fill()
b.circle(50)
b.end_fill()

b.up()
b.goto(180, 0)
b.down()

b.fillcolor('#FFEBCD')
b.begin_fill()
b.circle(50)
b.end_fill()

b.up()
b.goto(45, -50)
b.down()

b.fillcolor('#FFA07A')
b.begin_fill()
b.circle(50)
b.end_fill()

b.up()
b.goto(135, -50)
b.down()

b.fillcolor('#778899')
b.begin_fill()
b.circle(50)
b.end_fill()


time.sleep(10)
