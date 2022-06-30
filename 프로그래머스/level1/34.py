# 두 개 뽑아서 더하기
import itertools

def solution(numbers):
    answer = []

    for x in itertools.combinations(numbers, 2):
        n = sum(list(x))
        answer.append(n)

    result = list(set(answer))
    result.sort()

    return result