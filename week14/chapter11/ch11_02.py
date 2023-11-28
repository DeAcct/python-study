num = 10                         # 전역변수 num 선언


def fun1():
    num = 20	           # 지역변수 num 선언
    print('num : ', num)       # 지역변수 num 사용(함수 안에서 num을 먼저 찾는다.)


print('num : ', num)           # 전역변수 num 사용
# 함수호출 이하 코드 작성
fun1()


gConst = 10


def fun2():
    global gConst
    gConst = 30
    print(gConst)


print(gConst)  # 여기서는 10
fun2()  # 바뀌는 동작이 함수 내에 있으므로
print(gConst)  # 여기서는 30
