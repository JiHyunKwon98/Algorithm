# 왕실의 나이트

n = 8
location = input()
column = int(ord(location[0]) - int(ord('a'))) + 1
row = int(location[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_column = column + step[1]
    next_row = row + step[0]
    if next_column >= 1 and next_row >= 1 and next_column <= 8 and next_row <= 8:
        result += 1

print(result)