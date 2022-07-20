#영어 끝말잇기
def solution(n, words):
    answer = []

    count = dict()

    count[words[0]] = 1

    for i in range(1, len(words)):
        try:
            count[words[i]] += 1
        except:
            count[words[i]] = 1

        if count[words[i]] > 1 or words[i - 1][-1] != words[i][0]:
            x = (i + 1) % n
            y = (i + 1) / n
            if x == 0:
                x = n
            if y > (i + 1) // n:
                y += 1
            return [x, int(y)]
    else:
        return [0, 0]
