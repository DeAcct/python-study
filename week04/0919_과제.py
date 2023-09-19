'''
print("학교를 입력하세요")
school = input()
print("학과를 입력하세요")
major = input()
print("학번을 입력하세요")
studentId = input()
print("이름을 입력하세요")
name = input()
print(school, major, studentId, name)
'''

# print함수 연습
p = "파이썬"
j = "자바"
print(p + '     ' + j)
print(p + '' + j)
print(p, j)

# 다른 문장 속에 포함
print('개발언어에는'+p+','+j+'등이 있어요')
print('개발언어에는', p, ',', j, '등이 있어요')
# 문자열포맷 1.{} + format
print('개발언어에는 {}, {}등이 있어요'.format(p, j))
print('개발언어에는 {0}, {1}등이 있어요'.format(p, j))
print('개발언어에는 {1}, {0}등이 있어요'.format(p, j))
