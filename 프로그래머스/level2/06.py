#소수찾기
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


def solution(numbers):
    numbers = list(numbers)

    count = 0
    arr = []
    for i in range(len(numbers)):
        for x in itertools.permutations(numbers, i + 1):
            arr.append(int(''.join(list(x))))

    arr = list(set(arr))
    for i in arr:
        if is_prime_number(i):
            count += 1

    return count