# 문자열 내 p와 y의 개수
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

def solution(s):
    a = 0
    b = 0
    s = list(s)

    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            a += 1
        elif s[i] == 'y' or s[i] == 'Y':
            b += 1

    if a == b or (a == 0 and b == 0):
        return True
    else:
        return False