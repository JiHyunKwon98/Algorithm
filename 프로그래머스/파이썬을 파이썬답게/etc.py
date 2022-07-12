"""
for 문과 if문을 한번에 - List comprehension의 if 문
"""
# 1) 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]

"""
두 변수의 값 바꾸기 - swap
"""
# 1) a = 3, b = 'abc'를 a = 'abc', b = 3 으로 바꾸기
a = 3
b = 'abc'
a, b = b, a

"""
이진 탐색하기 - binary search
"""
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))