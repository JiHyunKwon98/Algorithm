def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i]:
            absolutes[i] = +absolutes[i]
        else:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)

def solution2(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer