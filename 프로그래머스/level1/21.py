# 문자열 다루기 기본
def solution(s):
    s = list(s)
    n = len(s)

    for i in range(n):
        if s[i].isdigit():
            s[i] = int(s[i])
        else:
            return False

    if n == 4 or n == 6:
        return True
    else:
        return False