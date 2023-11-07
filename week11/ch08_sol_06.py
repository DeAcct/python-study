fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print("fruits : ", fruits)

# 274 페이지 이하 코드 작성 - remove
for item in fruits:
    if item == "당근" or item == "토마토":
        fruits.remove(item)

print("fruits : ", fruits)
# print(f'fruits: {fruits}')
