# 1이 될 때까지 (답안 예시)
n, k = map(int, input().split())
result = 0  # 1, 2

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k  # 25 , 5, 1
    result += (n - target)  # 25 -25 = 0, 5-5 = 0 1-1 =0
    n = target  # 25, 5, 1
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:  # 25, 5, 1
        break
    # K로 나누기
    result += 1
    n //= k  # 25//5 = 5 , 5//5 = 1

# 마지막 으로 남은 수에 대하여 1씩 빼기
result += (n - 1)  # 3-1
print(result)  # 2
