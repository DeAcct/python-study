temp = int(input('기계 온도 입력: '))  # 정수형 변환

if temp >= 40:
    print('팬(Fan) 가동')
else:
    print('팬(Fan) 중지')

# 위내용에서 에러부분 확인 코드 수정 후  결과 확인
# 교재 184페이지 확인문제1 코드 입력 결과 확인
# 교재 184페이지 1번 작업
# number
number = int(input("양의 정수 입력"))
result = number / 3

if (result - int(result)) >= 0.5:
    result = int(result) + 1
else:
    result = int(result)

print("결과: ", result)


# 교재 184페이지 2번 작업
mileage = 1200
if (mileage >= 1000):
    print("마일리지 사용가능")
else:
    print("마일리지 사용불가")
