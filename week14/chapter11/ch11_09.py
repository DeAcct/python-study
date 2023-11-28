def addFunction(n1, n2):
    sum = n1 + n2
    return sum


result = addFunction(10, 20)
print(result)

# 곱하기 함수 선언, 연산 결과 호출하여 반환 출력하는 프로그램 추가 코딩 작성


def mul(n1, n2):
    return n1 * n2


mulRes = mul(200, 214)
print(mulRes)

# 교재 360p ch11_10.py  코드 작성 return 없이 수정


def addFunction2(n1, n2):
    print(n1 + n2)


addFunction2(90, 90)


# 교재 361p ch11_sol_03.py  코드 작성 / 사칙연산 프로그램 만들기
def calculator(num1, num2):
    if (num2 == 0):
        print("0으로 나눌 수 없어요!")
        return None
    plus = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    return (plus, minus, mul, div)


inputNum1 = int(input("첫 번째 정수를 입력하세요: "))
inputNum2 = int(input("두 번째 정수를 입력하세요: "))

result = calculator(inputNum1, inputNum2)
print(f"사칙연산 결과(가, 감, 승, 제): {result}")
