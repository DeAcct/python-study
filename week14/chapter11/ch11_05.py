def forecastWeather(temp, humi, rain):	      # 인수 3개를 매개변수 3개에 저장
    print('날씨 예보입니다.')
    print('최고 온도 : ', temp, '℃')
    print('평균 습도 : ', humi, '%')
    print('비올 확율 : ', rain, '%')


temperature = 32
humidity = 67
rainPercent = 50

forecastWeather(temperature, humidity, rainPercent)  # 함수 호출 시 인수 3개 전달

# 위 내용 실행 후
# 함수 호출시 부천대학교 본인학과 본인이름 인수 3개 전달하는 프로그램 작성


def univ_Info(school, depart, name):
    print('학생정보입니다..')
    print('학교  : ', school)
    print('학과  : ', depart)
    print('이름  : ', name)


school = "부천대학교"
depart = "디지털미디어디자인과"
name = "이현성"

univ_Info(school, depart, name)
