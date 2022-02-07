# 거스름 돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기  // : 몫 연산자
    n %= coin # % : 나머지 연산자

print(count)
