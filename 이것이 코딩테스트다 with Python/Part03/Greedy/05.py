# 볼링공 고르기
import itertools

n, m = map(int, input().split())

arr = list(map(int, input().split()))
a = 0
b = 0

for i in itertools.combinations(arr, 2):
    if list(i)[0] == list(i)[1]:
        b += 1
    a += 1

print(a-b)