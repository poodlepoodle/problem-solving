import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

string = input()
stack = deque()

for letter in string:
    if letter == ')':
        cnt = 0
        pull = stack.pop()
        while pull != '(':
            if pull[0] == 'x':
                cnt += int(pull[1:])
            else:
                cnt += 1
            pull = stack.pop()

        mul = int(stack.pop())
        stack.append('x' + str(mul * cnt))
    else:
        stack.append(letter)

    # print(q)

cnt = 0
for letter in stack:
    cnt += 1 if letter[0] != 'x' else int(letter[1:])
print(cnt)
