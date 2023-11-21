# scores = {'C/C++': 'A', 'Java': 'B+', '모바일': 'C',
#           '보안': 'A+', '해킹': 'F', '시스템': 'C+'}

# print('#시나리오1 ')
# print(scores)

# print('#시나리오2')
# print('Java : ', scores['Java'])
# print('시스템 : ', scores['시스템'])

# print('#시나리오3 ')
# scores['파이썬'] = 'A'
# scores['OS'] = 'A+'
# print(scores)

# print('#시나리오4')
# scores['Java'] = 'F'
# scores['시스템'] = 'A'
# print(scores)
# print()

# print('#시나리오5')
# # 이하 코드 작성
# for key in scores.keys():
#     print(f'{key}\t{scores[key]}')

scores = {
    "커뮤니케이션디자인1": "A",
    "브랜딩디자인1": "A+",
    "UI디자인 전략과 리서치": "A+",
    "웹코딩(Javascript, HTML)": "A+",
    "VR1": "A+",
    "3D디지털모델링 & 프린팅": "A+",
    "직업윤리": "A+",
    "나를 찾아가는 인문고전 읽기": "A+",
    "커뮤니케이션과 대인관계 능력": "A+"
}

print("시나리오 #1")
print(scores)

print("시나리오 #2")
print(scores["커뮤니케이션디자인1"])

print("시나리오 #3")
scores["브랜딩디자인2"] = "A+"
scores["파이썬을 이용한 코딩"] = "A+"
scores["웹디자인"] = "A+"
scores["디자인트렌드의 이해"] = "A+"
scores["커뮤니케이션디자인2"] = "A+"
scores["VR2"] = "A+"
scores["UI프로토타이핑"] = "A+"
print(scores)

print("시나리오 #4")
scores["커뮤니케이션디자인1"] = "A+"
print(scores)

print("\n")
print("시나리오 #5")
for key in scores.keys():
    print(f'{key:20s}{scores[key]}')

print("시나리오 #6")
del scores["브랜딩디자인2"]
del scores["파이썬을 이용한 코딩"]
del scores["웹디자인"]
del scores["디자인트렌드의 이해"]
del scores["커뮤니케이션디자인2"]
del scores["VR2"]
del scores["UI프로토타이핑"]
print(scores)

print("추가 #1")
scores_by_list = ["커뮤니케이션디자인1", "A",
                  "브랜딩디자인1", "A+",
                  "UI디자인 전략과 리서치", "A+",
                  "웹코딩(Javascript, HTML)", "A+",
                  "VR1", "A+",
                  "3D디지털모델링 & 프린팅", "A+",
                  "직업윤리", "A+",
                  "나를 찾아가는 인문고전 읽기", "A+",
                  "커뮤니케이션과 대인관계 능력", "A+"]
print(scores_by_list)

print("추가 #2")
scores_by_tuple = ("커뮤니케이션디자인1", "A",
                   "브랜딩디자인1", "A+",
                   "UI디자인 전략과 리서치", "A+",
                   "웹코딩(Javascript, HTML)", "A+",
                   "VR1", "A+",
                   "3D디지털모델링 & 프린팅", "A+",
                   "직업윤리", "A+",
                   "나를 찾아가는 인문고전 읽기", "A+",
                   "커뮤니케이션과 대인관계 능력", "A+")
print(scores_by_tuple)
