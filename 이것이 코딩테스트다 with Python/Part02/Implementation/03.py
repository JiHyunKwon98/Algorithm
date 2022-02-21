# 상하좌우 처음 풀이
n = int(input())

location = list((input().split()))

x, y = 1, 1

for i in range(len(location)):
    if (y > 1 and location[i] == 'L'):
        y -= 1
    elif (y < n and location[i] == 'R'):
        y += 1
    elif (x > 1 and location[i] == 'U'):
        x -= 1
    elif (x < n and location[i] == 'D'):
        x += 1

print(x, y)
