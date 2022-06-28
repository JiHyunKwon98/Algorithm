# 자연수 뒤집어 배열로 만들기
def solution(n):
    arr = [int(a) for a in str(n)]
    arr.reverse()

    return arr