# 최댓값 최솟값
def solution(s):
    answer = ''
    arr = [int(x) for x in s.split()]
    arr.sort()

    answer += str(min(arr)) + ' ' + str(max(arr))

    return answer


def solution1(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))