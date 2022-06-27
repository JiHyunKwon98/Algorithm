# 핸드폰 번호 가리기
def solution(phone_number):
    n = len(phone_number) - 4
    arr = []
    for i in range(n):
        arr.append("*")

    a = phone_number[-4:]
    arr.append(a)

    answer = ''.join(s for s in arr)

    return answer