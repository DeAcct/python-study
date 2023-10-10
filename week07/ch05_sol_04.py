weight = int(input('몸무게(kg) : '))     # 몸무게 입력
height = int(input('신장(m) : '))       # 신장 입력
# 형변환
bmi = float(weight / (height * height))
print('BMI :', bmi)
