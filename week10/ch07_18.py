num = 1
sum = 0

while num < 11:
    sum += num
    print("sum: ", sum)
    if sum >= 30:
        print('num : ', num)
        break
        # 프로그램 실행 후 이하 코드 작성
    num += 1
