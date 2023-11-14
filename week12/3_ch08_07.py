import turtle
import time

t = turtle.Turtle()
t.shape("turtle")

scores = [90, 75, 80, 100, 75]
xLength = 400
yLength = 200

t.forward(xLength)  # x축 그리기

t.up()
t.goto(0, 0)
t.down()

t.left(90)
t.forward(yLength)  # y축 그리기

t.up()
t.goto(30, 0)
t.down()


# 국어점수 그래프 그리기
t.fillcolor("#FF5733")
t.begin_fill()
t.forward(scores[0])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[0])
t.right(90)
t.forward(20)
t.end_fill()

t.up()
t.goto(90, 0)
t.down()

# 영어 점수 그래프 그리기
t.fillcolor("#FFA533")
t.begin_fill()
t.right(90)
t.forward(scores[1])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[1])
t.right(90)
t.forward(20)
t.end_fill()

t.up()
t.goto(150, 0)
t.down()


# 수학 점수 그래프 그리기
t.fillcolor("#D4FF33")
t.begin_fill()
t.right(90)
t.forward(scores[2])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[2])
t.right(90)
t.forward(20)
t.end_fill()

t.up()
t.goto(210, 0)
t.down()

# 파이썬 점수 그래프 그리기
t.fillcolor("#33FF71")
t.begin_fill()
t.right(90)
t.forward(scores[3])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[3])
t.right(90)
t.forward(20)
t.end_fill()

t.up()
t.goto(270, 0)
t.down()

# 자료구조 점수 그래프 그리기
t.fillcolor("#33ECFF")
t.begin_fill()
t.right(90)
t.forward(scores[4])
t.right(90)
t.forward(20)
t.right(90)
t.forward(scores[4])
t.right(90)
t.forward(20)
t.end_fill()

time.sleep(3)
