# tuple은 읽기 전용 순차 리스트
# 값을 수정할 수 없다.
# 슬라이싱, 인덱스 참조는 가능하다.
# len()함수를 쓸 수 있다.

"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)
"""

# packing - 묶어서 tuple로 만든다
# unpacking (tuple에서 사용 가능) - 묶은걸 푼다
# == [js] 구조분해할당

"""
(one, two, *three) = numbers
print(one)      # 1
print(two)      # 2
print(three)    # 나머지가 리스트로 출력됨 | [3,4,5,6,7,8,9,10]

(*others, nine, ten) = numbers
print(others)   # [1,2,3,4,5,6,7,8]
print(nine)     # 9
print(ten)      # 10

(one, *others, ten) = numbers
print(one)      # 1
print(others)   # [2,3,4,5,6,7,8,9]
print(ten)      # 10
"""

# set는 집합
# == [js] new Set()
# 중복할 수 없음
# 순서가 보장되지 않음

"""
setOne = {"돈까스", "쫄면", "김밥"}
setTwo = {"초밥", "우동", "돈까스"}
print(setOne, setTwo)
print(setOne.difference(setTwo))  # 차집합
"""

"""
my_set = {'파이썬', '자바', 'C언어'}
print(my_set[1])  # 접근 불가
my_set[1] = 'html'  # 수정 불가
"""

"""
my_list = ['파이썬', '자바', 'C언어']
my_list[1] = 'html'
print(my_list[1])

my_set = {'파이썬', '자바', 'C언어'}
print(my_set)
my_set.add("html")
print(my_set)       # 자료 추가 가능
my_set.remove("html")
print(my_set)       # 자료 삭제 가능
my_set.remove("자바")
print(my_set)
my_set.clear()
print(my_set)       # 비어 있는 set 출력
del my_set
"""
"""
print(my_set)       # 존재가 완전히 사라짐
"""

# dictionary
# [js] object와 비슷하나 문자열 이외의 자료도 key로 사용 가능하다.
Person = {
    "이름": "이현성",
    "나이": 20,
    "키": 180,
    "몸무게": 70
}
print(Person)
print(Person["이름"])
print(Person["나이"])
# 존재하지 않는 key에는 접근할 수 없다.
# print(Person["별명"])
# 존재 여부는 확인할 수 있다.
print(Person.get("별명"))
# 자료 추가 가능
Person["최종학력"] = "대학교"
print(Person)
# 자료 수정 가능
Person["키"] = 165
print(Person)
Person.update({"키": 170, "몸무게": 50})
print(Person)
# 자료 삭제 가능
Person.pop("몸무게")
print(Person)
# 초기화
Person.clear()
print(Person)   # 비어 있는 dictionary 출력
