sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for index, item in enumerate(sports):
    if index % 2 == 1:
        print(index, ' : ', item)
# 짝수아이템 출력 코드 수정 추가 작성

print("짝수만")
for index, item in enumerate(sports):
    if index % 2 == 0:
        print(f'{index}:{item}')

print("모두")
for index, item in enumerate(sports):
    print(f'{index}:{item}')
