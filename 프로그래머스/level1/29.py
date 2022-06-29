# 부족한 금액 계산하기
def solution(price, money, count):
    sum = 0

    for i in range(1, count + 1):
        sum += price * i

    if sum > money:
        return sum - money
    else:
        return 0

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))