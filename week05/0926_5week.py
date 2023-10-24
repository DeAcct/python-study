# 문자열 포맷
# 방법1
print("나는 %d살입니다." % 20)  # 정수
print("나는 만 나이로 %d살입니다." % 20)  # 정수

print("나는 %s을 좋아해요." % "파이썬")  # 문자열
print("나는 %s을 좋아해요." % "브랜딩디자인")  # 문자열

print("Apple은 %c로 시작해요.." % "A")  # 문자
print("사과는 %c로 시작해요.." % "사")  # 문자

# %s 는 뭐든...

print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 만 나이로 {}살입니다.".format(20))

print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {}색과 {}색을 좋아해요.".format("다홍", "짙은 토마토"))

print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))

print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 집에 갈 때 {0}탈까 {1}탈까 {2}탈까 고민합니다.".format("버스", "지하철", "택시"))
print("나는 집에 갈 때 {2}탈까 {0}탈까 {1}탈까 고민합니다.".format("버스", "지하철", "택시"))

# 방법3
print("나는 {col1}색과 {col2}색을 좋아해요.".format(col1="파란", col2="red"))
a = "초록"
b = "노랑"
c = "다홍"
print("나는 {color1}색과 {color2}색과 {color3}색을 좋아해요.".format(
    color1=a, color2=b, color3=c))
print("나는 {0}색과 {1}색과 {2}색을 좋아해요.".format(a, b, c))

# 탈출문자연습
# \n 줄바꿈
# \"   \' 문장내에서 ", ' 출력시
print("저는 '이현성' 입니다")
print('저는 "이현성" 입니다')
print("저는\"이현성\" 입니다")
print('저는\'이현성\' 입니다')
# \\ : 문장 내에서 \
print("c:\\Users\\NaCoding")
snack = '부천대학교\n디지털미디어디자인과\n이현성'
print(snack)

# \r : 커서를 맨 앞으로 이동
print("red Apple\rPine.")

# \t : 탭
print("red\tApple")
print("red\t\t\tApple")

# input() 1_연습
person1 = input()


# input() 2_연습 :  키보드로 숫자입력


# input() 3_연습 키보드로 숫자입력
# num3 = input("정수입력?")

# import random
# print(random.randint(1, 45))

# 1부터 45까지의 수중에서 랜덤하게 숫자 하나 출력
# print(random.randint(1, 45))
# 1부터 10까지의 숫자 중 3개의 숫자를 랜덤하게 중복없이 뽑아 출력하는 코드입니다.
# print(random.sample(range(1,10),3))
"""numbers=[]
for i in range(1,7):
  number=random.randint(1,45)
  numbers.append(number)
print(numbers)"""

name = "이현성"
height = 175.3181
print(f'제 이름은 {name}이고 키는 {height:.2f}')
