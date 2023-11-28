# # my_list = [1, 2, 3, 4, 5]
# # # my_list에서 3보다 큰 요소만 걸러내기
# # new_list = [x for x in my_list if x > 3]
# # print(f'my_list: {my_list}, new_list: {new_list}')


# # def book_price():
# #     print("10,000원")
# #     print("10,000원")


# # book_price()


# # def school():
# #     print("부천대학교")


# # school()

# # def book_price1(name):
# #     print(f"사랑하는 {name} 고객님을 위한 특가")
# #     print("python책 10,000원")


# # customer1 = '강감찬'
# # book_price1(customer1)

# # customer2 = "이승만"
# # book_price1(customer2)


# def get_price(isCoupon: bool = False) -> int:
#     # early return
#     if isCoupon:
#         return 8000
#     return 10000


# price = get_price(True)
# print(f"python책 {price}원")


# # [JS] function my_function(a, ...b){}
# def my_function(a, *b):
#     print(a, b)


# my_function(1, 2, 3, 4, 5, 6)


# message = "비밀"  # 전역변수


# def secret():
#     message = "이현성"  # 지역변수
#     print(message)


# print(message)  # 비밀(전역변수)
# secret()  # 이현성(지역변수)


# # print(message)


# message = "나는 전역 변수"
# print(message)


# def no_secret():
#     print(message)


# no_secret()  # 나는 전역 변수

message = "나는 전역 변수"
print(message)


def no_secret():
    message = "새로운 지역 변수"
    print(message)


no_secret()  # 새로운 지역 변수
print(message)  # 나는 전역 변수


def g_secret():
    global message  # 전역변수를 쓰겠다
    message = "나는 전역변수다!"
    print(message)


g_secret()  # 나는 전역변수다!
print(message)  # 나는 전역변수다!
