# 문자열 재정렬
n = input()
a = []
b = []

for i in n:
    if i.isdigit():
        a.append(int(i))
    else:
        b.append(i)

c = sum(a)
b.sort()
b.append(str(c))

for i in b:
    print(i, end='')