# 럭키 스트레이트
arr = list(map(int, input()))

a = 0
b = 0

for i in range(len(arr)):
    n = len(arr) / 2
    if i < n:
        a += arr[i]
    else:
        b += arr[i]

if a == b:
    print("LUCKY")
else:
     print("READY")