# 자물쇠 # 보류...
n = int(input())

first = []

for i in range(n):
    first.append(i)

array = list(map(int, input().split()))

temp = []

def left_push(n):
    first.extend(array[0:n])
    del first[0:n]

def reverse(p, q):
    temp.extend(array[p - 1: q])
    del first[p - 1: q]
    for i in range(len(temp)):
        first.insert(p - 1, temp[i])

while True:
    reverse

    if first == array:
        break
