myMoney = 5000
rate = 0.05

myMoney += myMoney * rate  # 1년 후 총 금액, 1)5000*0.05=250, 2)myMoney=5000+250
myMoney += myMoney * rate
myMoney += myMoney * rate
myMoney += myMoney * rate
myMoney += myMoney * rate

print('5년 후 총 수령액(소수점 미만 절삭) : ', int(myMoney), '원')
# 정수형 변환
