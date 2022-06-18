# 럭키 스트레이트
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
