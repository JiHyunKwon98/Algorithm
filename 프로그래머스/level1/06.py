# 자릿수 더하기
def solution(n):
    arr = [int(a) for a in str(n)]
    answer = sum(arr)

    return answer