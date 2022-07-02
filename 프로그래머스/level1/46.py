# 소수 만들기
import itertools
import math

def is_prime_number(num):
    if num < 2:
        return False
    else:
        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0:
                return False
        return True


def solution(nums):
    count = 0
    for x in itertools.combinations(nums, 3):
        if is_prime_number(sum(list(x))):
            count += 1

    return count