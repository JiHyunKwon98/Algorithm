# 최대 공약수와 최소 공배수
import math

def solution(n, m):
    a = math.gcd(n, m) # 최대 공약수 구하기
    b = n * m / a #  최소 공배수는 = 숫자 * 숫자 / 최대 공약수

    arr = []
    arr.append(a)
    arr.append(b)

    return arr

a = 10
b = 12

# 최대 공약수
for i in range(min(a,b), 0, -1):
    if a%i == 0 and b%i ==0:
        print(i)
        break

# 최소 공배수
for i in range(max(a,b), (a+b)+1):
    if i%a ==0 and i%b ==0:
        print(i)
        break