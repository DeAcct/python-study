# lang = "PYTHON"
# print(lang[0])
# print(lang[5])
# print(lang[-1])
# print(lang[1:6])

# snack = "노브랜드 나초칩"
# two = "두개"
# get = snack + two
# print(get)

# get += "주세요"
# print(get)

# num = 3
# num = num + 2
# print(num)
# num += 2
# print(num)
# num -= 2
# print(num)
# num *= 2
# print(num)
# num /= 2
# print(num)

# sub = "파이썬"
# print(len(sub))
# a = "디지털미디어디자인과"
# print(len(a))

"""
letter = "how are YOU"
print(letter.lower())       # 전부 소문자
print(letter.upper())       # 전부 대문자
print(letter.capitalize())  # 문장 맨 앞만 대문자
print(letter.title())       # 단어 맨 앞만 대문자
print(letter.swapcase())    # 대소문자 반전
print(letter.split())       # 비어있으면 스페이스 기준으로 나눔

print(letter.count("how"))  # 제공된 문자열이 몇 개 존재하는지 확인
"""

"""
s = "부천대학교"
print(s.startswith("부천"))  # 제공된 문자열로 시작하는지 True False
print(s.endswith("부천"))
print(s.strip("부천"))
print(s.endswith("부천"))
print(s.endswith("부천"))
"""

"""
my_list = ["Python", "CLang", "CPP", "CSharp", "Java",
           "GoLang", "Kotlin", "Kotlin", "JavaScript", "TypeScript"]
print(my_list)


your_list = ["Python", 3.14, True, "C", False, 100]
print(your_list)

empty_list = []
print(empty_list)
"""

"""
a_list = ["파이썬", "브랜딩디자인", "웹디자인"]
print(a_list)
# print(a_list[10])
print(a_list[0:2])
print("파이썬" in a_list)
"""

"""
my_list = ["파이썬", "C언어", "자바"]
print(my_list)
print(len(my_list))
my_list[1] = "HTML"
print(my_list)
my_list[2] = "부천대학교"
print(my_list)

my_list.append("타입스크립트")
print(my_list)
my_list.remove("파이썬")
print(my_list)
"""

univ_list = ["부천대학교", "디지털미디어디자인과", 2213024, "이현성"]
print(univ_list)
print(univ_list[1])
print(len(univ_list))
univ_list[3] = "이상민"
print(univ_list)
univ_list.append("이현성")
univ_list.remove(2213024)
print(univ_list)

your_list = [2213024, "윤석열", "이재명"]
univ_list.extend(your_list)
print(univ_list)
