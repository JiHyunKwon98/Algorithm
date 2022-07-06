# 신고 결과 받기
def solution(id_list, report, k):
    report = set(report)
    answer = {x: 0 for x in id_list}

    reports = {x: 0 for x in id_list}

    for x in report:
        reports[x.split()[1]] += 1

    for x in report:
        if reports[x.split()[1]] >= k:
            answer[x.split()[0]] += 1

    return list(answer.values())