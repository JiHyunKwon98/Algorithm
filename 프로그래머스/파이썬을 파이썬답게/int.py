"""
몫솨 나머지 - divmod
"""
# 1) 보통의 경우 나머지와 몫을 따로 구한다.
a = 7
b = 5
print(a//b, a%b)

"""
2) python에서는 divmod와 unpacking을 이용하면 된다.
"""
print(*divmod(a, b))

"""
n진법으로 표기된 string을 10진법 숫자로 변환하기 - int 함수 
"""
# 1) 보통의 경우는 for문을 이용해 숫자를 곱해가며 문제를 풉니다.
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)

"""
2) python에서는 int(x, base=10) 진법 변환을 지원한다.
"""
num = '3212'
base = 5
answer = int(num, base)

