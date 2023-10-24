from datetime import datetime                                     # 날짜 모듈 불러오기

print(datetime.now())  # 현재 날짜시간 출력

from datetime import date
print(date.today()) # 오늘 날짜 출력

from datetime import date,timedelta
start=date(2023,10,23)
finish=date(2023,10,26)
print((finish-start).days) # 두 날짜 사이의 일 수 계산하기

start=date(2023,10,23) ; h=timedelta(days=100)
print(start+h) # 100일 후 계산하기

from calendar import isleap
print(isleap(2023),isleap(2024)) # 윤년여부

import  time 
s=time.time()
for i in range(10):
    print(i)
e=time.time()
print(f'{e-s}초') # 실행시간 계산하기

#이하 코드 작업 교재 198페이지 코드입력 후 결과 확인 
