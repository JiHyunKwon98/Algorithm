# 곱하기 혹은 더하기 (강의)
a = input()
result = int(a[0])

for i in range(1, len(a)):
    # 두 수 중에서 하나라도 0혹은 1인 경우, 곱하기 보다는 더하기 수행
    num = int(a[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)