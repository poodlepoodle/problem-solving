from collections import deque
import sys

input = sys.stdin.readline

# N <= 5 * 10^5
N = int(input())

towers = list(map(int, input().rstrip().split()))

stack = deque()
answers = []

for idx, current in enumerate(towers):
    while stack and stack[-1][1] <= current:
        stack.pop()
    
    if not stack:
        answers.append(0)
    else:
        answers.append(stack[-1][0] + 1)
    stack.append((idx, current))
    
    # print(stack)
    # print(answers)
    # print()

print(" ".join(list(map(str, answers))))
