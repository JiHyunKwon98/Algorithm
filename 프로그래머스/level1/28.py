# 나머지가 1이 되는 수 찾기
def solution(n):
    arr = []

    for i in range(1, n):
        if n % i == 1:
            arr.append(i)

    answer = min(arr)

    return answer

def solution1(n):
    return [x for x in range(1,n+1) if n%x==1][0]

def solution2(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer