# 큰 수의 법칙 (처음 스스로 작성한 코드)
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a.reverse()

renew = [a[0], a[1]]

result = 0

while m >= 1:
    for i in range(k):
        result += int(renew[0])
        m -= 1
    result += int(renew[1])
    m -= 1

print(result)