# 리모컨
a, b = map(int, input().split())
c = abs(a-b)
count = 0

while c != 0:
    if c >= 10:
        c -= 10
        count += 1
    else:
        if c > 7:
            c += 1
            count += 1
        elif c > 4:
            c -= 5
            count += 1
        elif c > 2:
            c += 1
            count += 1
        else:
            c -= 1
            count += 1

print(count)