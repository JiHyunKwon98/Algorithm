# 가운데 글자 가져오기
def solution(s):
    n = len(s)
    a = n // 2

    if n % 2 != 0:
        return s[a]
    else:
        return s[a - 1:a + 1]