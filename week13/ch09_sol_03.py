scores = ('A', 'A+', 'B', 'B-', 'F', 'A++')

if 'F' in scores:
    print('경고')
# A+ 출력 코드 추가 작성
if "A+" in scores:
    print("참 잘했어요")

# tuple끼리 +연산자를 통해 결합하는 것은 가능하지만 .extend()메서드는 존재하지 않는다.
