"""
곱집합(Cartesian product) 구하기 - product
"""
# 1) 보통 사람들은 for 문을 이용해 두 iterable의 원소를 하나씩 곱해갑니다.
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)


# 2) itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))

"""
2차원 리스트를 1차원 리스트로 만들기 - from_iterable
"""
# 1) 보통 사람들은 반복문을 이용해 리스트를 더해갑니다.
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element

# 2) 파이썬 다양한 기능을 사용하면, for문을 사용하지 않고도 리스트를 이어 붙일 수 있습니다.
# 방법 1)
answer = sum(my_list, [])

# 방법 2)
[element for array in my_list for element in array]

"""
순열과 조합 - combinations, permutations
"""
# 1)  파이썬에서는
# itertools.permutation를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.
import itertools

pool = ['A', 'B', 'C']

print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

"""
가장 많이 등장하는 알파벳 찾기 - Counter
"""
# 1) 파이썬의 collections.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있습니다.
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0