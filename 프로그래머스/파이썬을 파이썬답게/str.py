"""
문자열 정렬하기
"""
# 1) 보통의 경우 for 문을 이용해 기존 스트링에 공백문자 (' ') 를 여러 번 붙이는 번거로운 일을 하지요
# ex) 우측 정렬 시
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)):
    answer += ' '
answer +=s

"""
2) 파이썬에서는 ljust, center, rjust와 같은 string 메소드를 사용해 코드를 줄일 수 있습니다.
"""
s.ljust(n) # 좌측 정렬
s.rjust(n) # 우측 정렬
s.center(n) # 가운데 정렬

"""
알파벳 출력하기 
"""
# 1) 손수 입력하는 방법 외
answer = 'abcdefghijk (편의상 생략)'

"""
2) 파이썬에서는 이런 데이터를 상수로 정의해놨다.
"""
import string

string.ascii_lowercase  # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters  # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789