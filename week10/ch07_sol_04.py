print(5, end='/')
print(3, end='    ')
print(5, end='')
print("부천대학교", end="")
print('파이썬')
for num in range(1, 10, 1):
    print(5, end='')
    print(' * ', end='')
    print(num, end='')
    print(' = ', end='')
    print(5 * num)

# 코드 실행 후 분석, 구구단 8단작성 추가 작업
for num2 in range(1, 10, 1):
    print("{0} * {1} = {2}".format(8, num2, num2 * 8))


userInput = int(input("구구단을 출력할 숫자를 입력하세요"))
for num3 in range(1, 10, 1):
    print("{0} * {1} = {2}".format(userInput, num3, userInput * num3))

sum1 = 0

for num in range(1, 11, 1):  # 추가 코드 작업
    sum1 += num

print("sum1 = ", sum1)

sum2 = 0

for num2 in range(1, 101, 1):  # 추가 코드 작업
    sum2 += num2

print("sum2 = ", sum2)
