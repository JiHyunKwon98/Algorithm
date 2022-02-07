# 1이 될 때까지 (처음 스스로 작성한 코드)
n, k = input().split()
n = int(n)
k = int(k)
min = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        min += 1
    n //= k
    min += 1

print(min)
