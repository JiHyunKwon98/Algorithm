# 모험가 길드
n = int(input())  # 모험가의 수
arr = list(map(int, input().split()))  # 모험가 길드의 공포도
arr.sort()
count= 0  # 현재 그룹에 포함된 모험가 수
result = 0 # 그룹 수

for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result) # 총 그룹 수 출력



