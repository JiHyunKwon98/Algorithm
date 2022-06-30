# 예산
def solution(d, budget):
    count = 0
    d.sort()

    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            count += 1

    return count