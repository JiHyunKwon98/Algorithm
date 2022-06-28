# 제곱근 판별 1
def solution(n):
    sqrt = n ** (1 / 2)  # 제곱근 구하기
    if sqrt % 1 == 0:  # x가 양의 정수일 경우 이 조건 만족
        return (sqrt + 1) ** 2

    return -1


# 제곱근 판별 2
import math

def solution(n):
    x = math.sqrt(n)
    if x % 1 == 0:
        answer = (x + 1) ** 2
    else:
        answer = -1

    return answer