# 최고의 피자
import math
n = int(input()) # 토핑 종류 수
a, b = map(int, input().split()) # a: 도우 가격, b : 토핑 가격
c = int(input()) # 도우 칼로리
array = []
kal_array = []

for i in range(n):
    m = int(input())
    array.append(m)

array.sort()
array.reverse()

pizza = c / a
kal = c
k = 0

for i in array:
    c += i
    k += 1
    result = c/(a+(b*k))
    if pizza <= result:
        pizza = result
    else:
        break

print(math.trunc(pizza))