# 3진법 뒤집기
def solution(n):
    result = ''

    while n:
        result += str(n % 3)
        n //= 3

    return int(result, 3)