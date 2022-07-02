# 숫자열과 문자열 단어
def solution(s):
    answer = ''

    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, num in enumerate(eng):
        if num in s:
            s = s.replace(num, str(i))
        answer = s

    return int(answer)