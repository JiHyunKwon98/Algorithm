# 부품 찾기

def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_serach(array, target, start, mid - 1)
    else:
        return binary_serach(array, target, mid + 1, end)

n = int(input())
arr = []
arr = list(map(int, input().split()))

m = int(input())
arr2 = []  # 찾고자 하는 target
arr2 = list(map(int, input().split()))

for i in arr2:
    result = binary_serach(arr, i, 0, n - 1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
