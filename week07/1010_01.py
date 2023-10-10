# 1교시 과제 - 사칙연산
# n1, n2, n3 변수 받기
# 계산 결과 변수는 s1, m1, mul1, div1, 나머지, 몫, 거듭제곱
n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))
n3 = int(input("세 번째 숫자를 입력하세요: "))

total = n1 + n2 + n3
minus = n1 - n2 - n3
multi = n1 * n2 * n3
div = n1 / n2 / n3
remain = n1 % n2 % n3
share = n1 // n2 // n3
power = n1 ** n2 ** n3

print('''
  덧셈: %d
  뺄셈: %d
  곱셈: %d
  나눗셈: %d
  나머지: %d
  몫: %d
  거듭제곱: %d
''' % (total, minus, multi, div, remain, share, power))
