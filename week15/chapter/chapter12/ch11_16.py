import turtle
import time

t = turtle.Turtle()
t.shape('circle')

# 매개변수 값에 따라 도형을 그리는 함수


def drawShapeByCoord(x, y):
    t.up()
    t.goto(x, y)
    t.down()

    num = int(input("원하는 도형을 입력하세요"))
    angle = 180 - (180 * (num-2))/num

    t.fillcolor("salmon")
    t.begin_fill()
    t.width(3)
    t.pencolor("orangered")
    for i in range(0, num):
        print(i)
        t.forward(50)
        t.left(angle)
    t.end_fill()


drawShapeByCoord(0, -150)
time.sleep(10)
