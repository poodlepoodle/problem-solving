# 백준 15927번: 회문은 회문아니야!! (2회차)

import sys

input = sys.stdin.readline

# len(string) <= 5 * 10^5
string = input().rstrip()

# 1. 스택
# 2. DP

# 팰린드롬이 아닌 조건은?
# ABCBA
# -> ABCBAC
# ABBA
# -> ABBAC
# 한 글자만 추가해도 팰린드롬...

# 특정 문자열이 팰린드롬이라면 팰린드롬이 아니게 하려면?

is_palindrome = True
left, right = 0, len(string) - 1
while left <= right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left, right = left + 1, right - 1

is_all_same_letter = True
first_letter = string[0]
for letter in string[1:]:
    if first_letter != letter:
        is_all_same_letter = False
        break

if is_all_same_letter: print(-1)
elif is_palindrome: print(len(string) - 1)
else: print(len(string))
