# 비밀지도
def solution(n, arr1, arr2):
    bin1 = [format(i, 'b').zfill(n) for i in arr1]
    bin2 = [format(i, 'b').zfill(n) for i in arr2]

    arr = []
    s = ''

    for a, b in zip(bin1, bin2):
        for i in range(n):
            if int(a[i]) == 1 or int(b[i]) == 1:
                arr.append("#")
            else:
                arr.append(" ")
        s = "".join(arr)

    result = list(map("".join, zip(*[iter(s)] * n)))

    return result