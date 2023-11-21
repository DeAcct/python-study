def book_price():
    print("파이썬 책 가격은 10000원 입니다.")


book_price()

# 2
customer1 = "강감찬"
print(f"{customer1} 고객님")
print("파이썬 책 가격은 10,000원 입니다.")

customer2 = "홍길동"
print(f"{customer2} 고객님")
print("파이썬 책 가격은 10,000원 입니다.")

# 3


def book_price1():
    print("파이썬책 가격은 10,000원 입니다.")


customer1 = "강감찬"
print(f"{customer1} 고객님")
book_price()

customer2 = "홍길동"
print(f"{customer2} 고객님")
book_price()

# 4


def success(name):
    print(f'{name}학생')
    print("파이썬 수강 성공")


name = "이현성"
success(name)
