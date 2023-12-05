# class BlackBox():
#     pass


# b1 = BlackBox()
# b1.name = "현성"
# print(b1.name)
# # b1은 BlackBox 객체인가요?
# print(isinstance(b1, BlackBox))

# # 객체지향의 시작...

# b2 = BlackBox()
# b2.name = "미래"
# print(b2.name)

class BlackBox():
    # self는 this와 거의 비슷한듯
    name: str
    price: int

    # [js] constructor()메서드와 비슷한 역할. 초기화 메서드
    def __init__(self, name, price):
        self.name = name
        self.price = price


b1 = BlackBox("치즈케이크", 200000)
print(b1.name, b1.price)
b2 = BlackBox("딸기케이크", 100000)
print(b2.name, b2.price)
