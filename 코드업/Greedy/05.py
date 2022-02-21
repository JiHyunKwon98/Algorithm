# 펜션
n, m = map(int, input().split())  # n : 여름 총 성수기 기간(1~n), m : 방의 개수(1~m)

array = [['X'] * m]  # 날짜를 편하게 확인 하기 위해서 0번째 줄은 임의로 추가

for i in range(n):
    array.append(list(input()))

s, t = map(int, input().split())  # s : 펜션에 도착하는 날, t : 떠나는 날

# maxday를 찾기 위해 행 우선으로 탐색
def check(n):
    maxday = 0
    for i in range(m):
        day = 0
        for j in range(n, t):
            if array[j][i] == 'O':
                day += 1
            else:
                break
        if maxday < day:
            maxday = day
    return maxday

count = -1
today = s

while today < t:
    stay = check(today)
    if stay == 0:
        count = -1
        break
    count += 1
    today += stay

print(count)
