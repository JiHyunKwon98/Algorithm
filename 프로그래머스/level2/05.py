#N개 최소공배수
import math

def gcm(a, b):
    return a*b // math.gcd(a, b)

def solution(arr):
    answer = 1
    for i in arr:
        answer = gcm(i, answer)
    return answer