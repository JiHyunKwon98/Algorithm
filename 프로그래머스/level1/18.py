# 두 정수 사이의 합
def solution(a, b):
    answer = 0

    n = max(a, b)
    m = min(a, b)

    for i in range(m, n + 1):
        answer += i

    return answer