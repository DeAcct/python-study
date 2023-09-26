# input() 1_연습
import random
person1 = input()
print("이름을 입력하세요: ")
person2 = input()
person3 = input("이름을 입력하세요: ")
print(person1+person2+person3)
print("내 이름은 {0}, 내 친구는 {1}, 또 다른 친구는 {2}이다.".format(
    person1, person2, person3))


# input() 2_연습 :  키보드로 숫자입력
num1 = input("정수입력: ")
num2 = input("정수입력: ")
sum1 = num1 + num2
print(sum1)


# input() 3_연습 키보드로 숫자입력
num1 = input("정수입력: ")
num2 = input("정수입력: ")
sum1 = float(num1) + float(num2)
print(sum1)

print(random.randint(1, 45))

# 1부터 45까지의 수중에서 랜덤하게 숫자 하나 출력
print(random.randint(1, 45))
# 1부터 10까지의 숫자 중 3개의 숫자를 랜덤하게 중복없이 뽑아 출력하는 코드입니다.
print(random.sample(range(1, 10), 3))
"""numbers=[]
for i in range(1,7):
  number=random.randint(1,45)
  numbers.append(number)
print(numbers)"""
