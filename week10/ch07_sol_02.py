# num 변수에 메일 발생 횟수 입력 받는 코드 작성
num = int(input("메일 발송 횟수를 입력하세요"))
for num in range(1, num+1, 1):
    print('메일 발송!')
