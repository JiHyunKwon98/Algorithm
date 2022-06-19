# 행렬의 덧셈
def solution(arr1, arr2):
    a = 0
    arr = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        arr.append(temp)

    answer = arr

    return answer