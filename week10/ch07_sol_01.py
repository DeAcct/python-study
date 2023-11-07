for num1 in range(1, 10, 2):
    print('num = ', num1)

b = int(input('숫자입력'))
for num2 in range(b, 10, 2):
    print('num2 = ', num2)

# 2~8 사이의 짝수 출력하기
# 교재보고 추가 코딩

for num3 in range(2, 10, 2):
    print(num3)

u_in = int(input("숫자입력"))
for num4 in range(u_in, 10, 1):
    if (num4 % 2 == 0):
        print(num4, "짝수")
        continue
    print("홀수")
