"""
sequence 멤버를 하나로 이어붙이기 - join
"""
# 1) 보통 사람들은 for 문을 이용해 원소를 하나씩 이어 붙입니다.
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value

# 2) 파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있습니다 .
my_list = ['1', '100', '33']
answer = ''.join(my_list)

"""
삼각형 별찍기 - sequence type의 * 연산
"""
# 1) 보통 사람들은 for 문을 이용해 기존 스트링에 'abc'를 여러 번 붙이는 번거로운 일을 하지요.
answer = ''
n = 4
for _ in range(n):
    answer += 'abc'

# 2) 파이썬에서는 *연산자를 사용해 코드를 획기적으로 줄일 수 있습니다.
answer = 'abc' * n

# 2-1) 또, * 연산자를 이용하면 [123, 456, 123, 456, 123 ...] 과같이 123, 456이 n번 반복되는 리스트를 만들 수 있습니다.
answer= [123, 456] * n