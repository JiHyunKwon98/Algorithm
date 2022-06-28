# 이상한 문자 만들기
def solution(s):
    a = s.split(' ')
    arr = []

    for i in range(len(a)):
        n = len(a[i])
        s = list(a[i])
        for j in range(n):
            if j % 2 != 0:
                s[j] = s[j].lower()
            else:
                s[j] = s[j].upper()

        string = ''.join(s)
        arr.append(string)

    result = ' '.join(arr)

    return result