color1 = ['red', 'yellow', 'white']
color2 = ['blue', 'purple', 'black']

# 269페이지 이하 코드 작성 extend
color1.extend(color2)
print(f'color1: {color1}')

color1 = ['red', 'yellow', 'white']
color2 = ['blue', 'purple', 'black']
color1 = color1 + color2
print(f'color1: {color1}')

color1.append("연어")
print(f'color1: {color1}')

color1.insert(2, "에메랄드 그린")
print(color1)

color1.pop(2)
print(color1)

del color1[2]
print(color1)

color1.remove("blue")
print(color1)
