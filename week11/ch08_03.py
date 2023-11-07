balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']

# 261페이지 이하 코드 작성 - for문
for ball in balls:
    print(f"for_ball: {ball}")


# 262페이지 이하 코드 작성 - while문
index = 0
while (index < len(balls)):
    print(f"while_ball: {balls[index]}")
    index += 1


# 264페이지 이하 코드 작성 - 확인문제1 , index
sports = ["baseball", "basketball", "tennis", "golf", "soccer"]
print(f"마지막 인덱스: {len(sports) - 1}")


# 264페이지 이하 코드 작성 - 확인문제2 , index
language = ["c/c++", "c#", "python", "java"]
print(f"""\"python\"의 인덱스: {language.index("python")}""")
