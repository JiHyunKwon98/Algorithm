# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    # 음식을 다 먹은 경우 더 먹을 것이 없을 때
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key=lambda x: x[1])  # 음식 번호 기준으로 정렬

    return result[(k - sum_value) % length][1]