# 성적이 낮은 순서로 학생 출력하기
n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]

student = sorted(array, key=setting)
result = [x[0] for x in student]

for i in result:
    print(i, end=' ')
