# 백준 2504번: 괄호의 값

from collections import deque
import sys

input = sys.stdin.readline

letters = deque(input().rstrip())
stack = deque([])

brackets = ('(', '[')
wrong = False

for current in letters:
    # print('new:', current)
    if current == ')':
        temp = 0
        temp_cnt = 0

        while stack and stack[-1] not in brackets:
            top = stack.pop()
            temp += top
            temp_cnt += 1
        
        if stack and stack[-1] == '(':
            stack.pop()
            if temp_cnt != 0:
                stack.append(2 * temp)
            else:
                stack.append(2)
        else:
            wrong = True
            break
    elif current == ']':
        temp = 0
        temp_cnt = 0

        while stack and stack[-1] not in brackets:
            top = stack.pop()
            temp += top
            temp_cnt += 1
        
        if stack and stack[-1] == '[':
            stack.pop()
            if temp_cnt != 0:
                stack.append(3 * temp)
            else:
                stack.append(3)
        else:
            wrong = True
            break
    else:
        stack.append(current)

    # print(*list(stack))
    # print()

answer = 0
for item in stack:
    if item in brackets:
        wrong = True
        break
    else:
        answer += item

print(answer if not wrong else 0)
