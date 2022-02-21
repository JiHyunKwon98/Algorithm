# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 처음 푼 풀이

s = input()
alpha = []
num = []
sum = 0
han = ''

for i in range(len(s)):
    if s[i].isalpha():
        alpha.append(s[i])
        alpha.sort()
    elif s[i].isdigit():
        num.append(s[i])

for digit in num:
    sum += int(digit)

for a in alpha:
    han += str(a)

print(han+str(sum))