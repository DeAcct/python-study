class Calculator:				       # 클래스 선언

    def __init__(self, n1, n2):		                    # 속성 정의
        print('\n=== __init__() START ===')
        self.num1 = n1
        self.num2 = n2

    def add(self):				       # 메서드 정의
        print('\n=== add() START ===')
        print('num1 + num2 =', self.num1 + self.num2)

    def subtract(self):			       # 메서드 정의
        print('\n=== subtract() START ===')
        print('num1 - num2 =', self.num1 - self.num2)

calc1 = Calculator(10, 20)		# 객체 생성
calc2 = Calculator(100, 200)  	# 객체 생성
calc3 = Calculator(1000, 2000)	# 객체 생성
