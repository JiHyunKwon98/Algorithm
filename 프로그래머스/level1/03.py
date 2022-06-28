# 하샤드 수
def solution(x):
    arr = [int(a) for a in str(x)]
    n = sum(arr)

    if x % n == 0:
        answer = True
    else:
        answer = False

    return answer