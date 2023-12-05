import turtle
import time

t = turtle.Turtle()
t.shape("circle")

# 매개변수 값에 따라 도형을 그리는 함수
# 색깔도 채워지도록


def drawShape(n):
    angle = 180 - (180 * (n-2)) / n

    t.fillcolor("salmon")
    t.begin_fill()
    t.width(3)
    for i in range(0, n):
        print(i)
        t.forward(100)
        t.left(angle)
    t.end_fill()


num = int(input("원하는 도형을 입력하세요"))
drawShape(num)

time.sleep(10)
