def fun1():
    print('fun1 함수를 호출합니다!')


def fun2():
    print('fun2 함수를 호출합니다!')


def fun3():
    # 이하 코드 작성
    fun1()
    fun2()
    print('fun3 함수를 호출합니다!')


# 이하 코드 작성
fun3()

# 교재 337페이지 확인문제 이하 코드 작성 함수명은 각자 설정


def printMemberInfo():
    getMemberFromDB()
    print("회원정보를 출력한다.")


def getMemberFromDB():
    connectDB()
    selectMemberFromDB()
    print("데이터베이스에서 회원정보를 가져온다")


def connectDB():
    print("데이터베이스에 접속한다.")


def selectMemberFromDB():
    print("데이터베이스에서 회원정보를 검색한다.")


printMemberInfo()
