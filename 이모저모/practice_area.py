# 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

array = [i * i for i in range(1, 10)]
# 1부터 9까지의 수의 제곱 값을 포함
print(array)

# N*M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for i in range(n)]
print(array)

a = [1, 2, 3]
print(a)
a.append(2)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
a.insert(2, 3)
print(a)
print(a.count(3))
a.remove(1)
print(a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

data = 'Hello World'
print(data)
data = "Dont't you know \"Python\""
print(data)

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b)
print(a & b)
print(a - b)

data = set([1, 2, 3])
print(data)

data.add(4)
print(data)
data.update([5, 6])
print(data)
data.remove(3)
print(data)

x = 15
if x >= 10:
    print(x)

# pass 조건문의 값이 True여도 아무것도 처리하고 싶지 않을 떄
score = 85

if score >= 80:
    pass # 나중에 작성
else:
    print("성적이 80점 미만")

print("프로그램 종료")

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

resutl = 0
for i in range(1, 10):
    result += i

print(result)
# ragne()의 값을 하나의 값만 넣으면 자동으로 시작값은 0이 된다.

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# continue: 반복문의 처음으로 돌아감

scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
    if i+1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()

def add(a, b):
    return a + b
print(add(3, 7))

def add(a, b):
    print("함수의 결과", a + b)
add(3, 7)
add(b = 3, a = 7)

# 함수 안에서 함수 밖의 변수 데이터를 변경해야하는 경우 -> global 키워드로 변수를 지정한다.

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

def add(a, b):
    return a+b

print((lambda a, b: a+b)(3,7))

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

import sys
data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print("정답은" + str(answer)+"입니다.")
print("정답은", str(answer),"입니다.")

result = sum([1, 2, 3, 4, 5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3+5)*7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

data = [9, 1, 8, 5, 3]
data.sort()
print(data)

n = ord(input())
print(n)

# chr() 정수값 -> 문자
# ord() 문자 -> 정수값

a = float(input())
print(format(a, ".2f"))

f = float(input())
print(round(f, 2))

n, m = input().split()
n = int(n)
m = int(m)

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

a = input()
n = int('F', 16)
result = int('F', 16)

for i in range(1, result+1):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

n = int(input())
d = [[0 for j in range(20)] for i in range(20)]

for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

