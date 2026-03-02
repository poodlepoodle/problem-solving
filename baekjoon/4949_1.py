# 백준 4949번: 균형잡힌 세상

import sys

input = sys.stdin.readline

# 문자열이 최대 몇 개 들어오는지 입력에서 안 알려줬는데??
# 각 문자열의 길이 <= 10^2

stack = []

while True:
    string = input().rstrip()

    if string == '.': break

    balanced = True
    stack.clear()

    for letter in list(string):
        if letter == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
        elif letter == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif letter in ['[', '(']:
            stack.append(letter)

    if stack: balanced = False
    print('yes' if balanced else 'no')
