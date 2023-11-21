from time import sleep

import turtle
t = turtle.Turtle()
turtle.bgcolor("beige")
t.width(2)
t.shape('arrow')

datas = [
    {
        "startX": -300,
        "startY": 0,
        "fillColor": "#DFFF00",
        "sides": 3
    },
    {
        "startX": -150,
        "startY": 0,
        "fillColor": "#FFBF00",
        "sides": 4
    },
    {
        "startX": 0,
        "startY": 0,
        "fillColor": "#FF7F50",
        "sides": 5
    },
    {
        "startX": 150,
        "startY": 0,
        "fillColor": "#DE3163",
        "sides": 6
    },
    {
        "startX": 300,
        "startY": 0,
        "fillColor": "#9FE2BF",
        "sides": 8
    }
]


def drawShape(shapeData):
    t.up()
    t.goto(shapeData["startX"], shapeData["startY"])      # x, y좌표 설정
    t.down()
    t.fillcolor(shapeData["fillColor"])
    t.begin_fill()

    for _ in range(shapeData["sides"]):  # 회전하면서 그리기
        t.forward(50)
        t.left(360 / shapeData["sides"])

    t.end_fill()


for shapeData in datas:
    drawShape(shapeData)


sleep(10)

# datas = [(-300, 0, "#DFFF00", 120, 120, 120), (-150, 0, "#FFBF00", 90, 90, 90, 90),
#          (0, 0, "#FF7F50", 72, 72, 72, 72, 72), (150, 0, "#DE3163", 60, 60, 60, 60, 60, 60), (300, 0, "#9FE2BF", 45, 45, 45, 45, 45, 45, 45, 45)]

# datas.reverse()
# for points in datas:
#     t.up()
#     t.goto(points[0], points[1])      # x, y좌표 설정
#     t.down()
#     t.fillcolor(points[2])
#     t.begin_fill()

#     for num in range(3, len(points)):  # 회전하면서 그리기
#         t.forward(50)
#         t.left(points[num])

#     t.end_fill()
# x, y좌표 및 회전각도 데이터 :  좌표값 다르게 지정 8각형 추가 , 확인문제 참고 하여 색상도 지정하여 작업
# Shape{startX:number, startY:number, angle1:number, angle2:number, angle3:number ...}
# datas<tuple<Shape>>
# datas = [(0, 0, 120, 120, 120), (100, 0, 90, 90, 90, 90),
#          (200, 0, 72, 72, 72, 72, 72), (300, 0, 60, 60, 60, 60, 60, 60)]

# for points in datas:
#     t.up()
#     t.goto(points[0], points[1])      # x, y좌표 설정
#     t.down()

#     for num in range(2, len(points)):  # 회전하면서 그리기
#         t.forward(50)
#         t.left(points[num])
