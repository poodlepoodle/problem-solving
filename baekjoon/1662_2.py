# 백준 1662번: 압축 (2회차)

import sys

input = sys.stdin.readline

# len(S) <= 50
S = input().rstrip()

stack = []

# for letter in S:
for idx, letter in enumerate(S):
    # print(S)
    # for i in range(idx):
    #     print(' ', end='')
    # print('^', end='')
    # for i in range(idx + 1, len(S)):
    #     print(' ', end='')
    # print()

    if letter == ')':
        cnt = 0
        while stack and stack[-1] != '(':
            middle = stack.pop()
            if middle[0] == '*':
                cnt += int(middle[1:])
            else:
                cnt += 1
        stack.pop() # '('

        front = stack.pop()
        # print('front:', front)
        # print('cnt:', cnt)
        # print('front * cnt:', front * cnt)
        stack.append(f'*{int(front) * cnt}')
    else:
        stack.append(letter)
    # print('stack:', stack)
    # print()
    # print()

answer = 0
while stack:
    s = stack.pop()
    if s[0] == '*':
        answer += int(s[1:])
    else:
        answer += 1
print(answer)
