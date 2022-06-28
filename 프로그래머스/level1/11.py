# 정수 내림차순으로 배치하기
def solution(n):
    arr = [int(a) for a in str(n)]
    arr.sort(reverse=True)

    s = ''.join(map(str, arr))

    return int(s)