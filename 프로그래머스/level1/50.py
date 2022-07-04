# 신규 아이디 추천
import re
def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i

    answer = re.sub(r"\.+", ".", answer)
    answer = answer.strip(".")

    if answer == "":
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = answer.strip(".")

    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    return answer