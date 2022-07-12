# 가장 많이 등장하는 알파벳 찾기
"""
input	output
'aab'	'a'
'dfdefdgf'	'df'
'bbaa'	'ab'
"""

import collections

my_str = input().strip()

answer = []

count  = collections.Counter(my_str)

max_value = max(list(count.values()))

for key in list(count.keys()):
    if count[key] == max_value:
        answer.append(key)

answer.sort()
print(''.join(answer))

