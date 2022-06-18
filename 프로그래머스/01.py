# JadenCase 문자열 만들기
def solution(s):
    answer = ''

    arr = list(s)

    if arr[0].isalpha() and arr[0].lower():
        arr[0] = arr[0].upper()

    for i in range(1, len(arr)):
        if arr[i - 1] == ' ' and arr[i].isalpha():
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()

    answer = ''.join(s for s in arr)

    return answer