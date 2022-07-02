#폰켓몬
def solution(nums):
    n = len(nums) // 2
    set_nums = list(set(nums))

    if len(set_nums) >= n:
        return n

    elif len(set_nums) < n:
        return len(set_nums)

def solution1(ls):
    return min(len(ls)/2, len(set(ls)))