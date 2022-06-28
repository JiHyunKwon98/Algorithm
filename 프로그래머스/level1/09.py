# 제일 작은 수 제거하기
def solution(arr):
    answer = []

    if len(arr) > 1:
        n = min(arr)
        arr.remove(n)
        answer = arr.copy()
    else:
        answer.append(-1)

    return answer