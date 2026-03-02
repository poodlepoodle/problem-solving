# 백준 2504번: 괄호의 값 (2회차)

import sys

input = sys.stdin.readline

# 1 <= len(string) <= 30
string = list(input().rstrip())

stack = []
answer = 0
balanced = True

braces = list('()[]')

for letter in string:
    # print(letter)
    if letter == ']':
        sums = 0
        while stack and stack[-1] not in braces:
            sums += stack.pop()
        
        if not stack or stack[-1] != '[':
            balanced = False
            break

        stack.pop() # '['
        stack.append(sums * 3 if sums > 0 else 3)

    elif letter == ')':
        sums = 0
        while stack and stack[-1] not in braces:
            sums += stack.pop()
        
        if not stack or stack[-1] != '(':
            balanced = False
            break

        stack.pop() # '('
        stack.append(sums * 2 if sums > 0 else 2)
        
    else:
        stack.append(letter)

    # print(stack)
    # print()

if not balanced: print(0)
else:
    for number in stack:
        if number in ['[', ']', '(', ')']:
            answer = 0
            break

        answer += number
    print(answer)
