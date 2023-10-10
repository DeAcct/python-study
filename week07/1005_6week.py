# 문자열 포맷
# 방법1
#print("나는 %d살입니다." % 20) #정수

#print("나는 %s을 좋아해요." % "파이썬") #문자열

#print("Apple 은  %c 로 시작해요.." % "A") #문자 

#%s 는 뭐든...

#print("나는 %s살입니다." % 20)

#print("나는 %s색과 %s색을 좋아해요."("파란","빨간"))

#방법2
# print("나는 {}살입니다.".format(20))

# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))

# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))

# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# 방법3
# print("나는 {col1}색과 {col2}색을 좋아해요.".format(col1="파란", col2="red"))

#탈출문자연습
# \n 줄바꿈
# \"   \' 문장내에서 ", ' 출력시
print("저는 '홍길동' 입니다")
# print('저는 "홍길동" 입니다')
# print("저는\"홍길동\" 입니다")
# print('저는\'홍길동\' 입니다')
# \\ : 문장 내에서 \

# \r : 커서를 맨 앞으로 이동
# print("red Apple\rPine.")

# \t : 탭
# print("red\tApple")

# input() 1_연습






# input() 2_연습 :  키보드로 숫자입력




# input() 3_연습 키보드로 숫자입력
num3=input("정수입력?")


# import random
# print(random.randint(1, 45))

# 1부터 45까지의 수중에서 랜덤하게 숫자 하나 출력
#print(random.randint(1, 45))
# 1부터 10까지의 숫자 중 3개의 숫자를 랜덤하게 중복없이 뽑아 출력하는 코드입니다.
#print(random.sample(range(1,10),3))
"""numbers=[]
for i in range(1,7):
  number=random.randint(1,45)
  numbers.append(number)
print(numbers)"""











