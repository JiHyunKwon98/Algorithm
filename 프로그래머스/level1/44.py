#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    arr = list(set(lottos) & set(win_nums))  # 일치하는 값 구하기

    a = len(arr) + lottos.count(0)  # 최대 당첨 값
    b = len(arr)  # 최소 당첨 값

    if b == 0 or b == 1:
        b = 1

    if a == 0:
        a = 1

    result = []

    result.append(abs(7 - a))
    result.append(abs(7 - b))

    return result