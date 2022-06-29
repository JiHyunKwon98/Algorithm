#서울에서 김서방 찾기
def solution(seoul):
    num = 0

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = i

    answer = "김서방은 {}에 있다".format(num)

    return answer