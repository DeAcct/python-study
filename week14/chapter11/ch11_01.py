num = 10                            # 전역변수 num 선언
# 이하 코드 작성 함수 선언 /   전역변수 num 사용


def fun1():
    print('num : ', num)	 # 전역변수 num 사용


# 이하 코드 작성 함수 호출
print('num : ', num)	 # 전역변수 num 사용
fun1()


# 위내용 실행 후 num1 이라는 전역변수에 50이라는 값 선언 후
# 함수 선언 num1 전역변수 사용 호출하여 출력하는 프로그램 작성
num1 = 50


def fun2():
    print(f'num1:{num1}')


print(f'num1:{num1}')
fun2()
