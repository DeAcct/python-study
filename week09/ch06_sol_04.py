peopleNumber = int(input('인원수를 입력하세요. '))

if peopleNumber == 1:
    print('400,000원 지원')
elif peopleNumber == 2:
    print('600,000원 지원')
elif peopleNumber == 3:
    print('800,000원 지원')
elif peopleNumber >= 4:
    print('1,000,000원 지원')
else:
    print("당신은 진정한 애국자... 2,000,000원 지원")

# 추가코딩해보세요.
# 입력 받는 값이 1이면 파이썬 2면 C언어 3이면 JAVA 4이상이면 없음
studyCode = int(input("언어 코드를 입력하세요"))

if studyCode == 1:
    print("파이썬")
elif studyCode == 2:
    print("C언어")
elif studyCode == 3:
    print("JAVA")
else:
    print("없음")
