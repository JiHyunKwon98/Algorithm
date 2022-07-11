"""
2차원 리스트 뒤집기 *** zip ***
"""
# 1) 보통은 다음과 같이 2중 for문을 이용해 리스트의 row와 column을 뒤집습니다.

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        new_list[i].append(my_list[j][i])

# 2) 파이썬에서는 zip과 unpacking을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.
new_list= list(map(list, zip(*my_list)))

"""
* zip 함수에 대해 
- zip(*iterables)는 각 iterable의 요소들을 모으는 이터레이터를 만듭니다.
- 튜플의 이터레이터를 돌려주는데, i번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i번째 요소를 포함합니다.
"""
mylist = [1, 2, 3]
newlist = [40, 50, 60]

for i in zip(mylist, newlist):
    print(i)

# (1, 40)
# (2, 50)
# (3, 60)

"""
사용 예 1) 여러 개의 Iterable 동시에 순회할 때 사용
"""
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []

for number1, number2, number3 in zip(list1, list2, list3):
    print(number1, number2, number3)

"""
사용 예 2) key리스트롸 value 딕셔너리 생성하기 
"""
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))  # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}

"""
모든 멤버의 type 변환하기 - map
"""
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
