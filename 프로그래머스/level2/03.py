# 최솟값 만들기
def solution(A, B):
    arr = []
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        n = A[i] * B[i]
        arr.append(n)

    answer = sum(arr)

    return answer