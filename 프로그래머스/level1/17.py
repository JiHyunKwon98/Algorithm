# 수박수박수박수박수박수?
def solution(n):
    a = '수'
    b = '수박'
    s = ''

    if n % 2 != 0:
        s = b * (n // 2) + a
    else:
        s = b * (n // 2)

    return s