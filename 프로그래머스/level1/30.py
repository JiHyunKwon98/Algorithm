# 최소 직사각형
def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])

    w = max(x[0] for x in sizes)
    h = max(x[1] for x in sizes)

    return w * h

def solution1(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
