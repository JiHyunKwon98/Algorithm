# 피보나치 수
def solution(n):
    d = [0, 1, 1]

    for i in range(3, n + 1):
        d.append((d[i - 1] + d[i - 2]) % 1234567)

    return d[-1]