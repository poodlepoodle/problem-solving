from collections import deque
import sys

input = sys.stdin.readline

# N <= 5 * 10^4
N = int(input())

# 1. 스택 쓰는 문제인 것 같은 느낌적인 느낌
# 2. 바뀌는 고도로 0이 들어오면 모든 빌딩 리셋

stack = deque([0])
answer = 0

# x <= 10^6, y <= 5 * 10^5
for _ in range(N):
    x, y = map(int, input().rstrip().split())

    if stack[-1] > y:
        while stack[-1] > y:
            stack.pop()
            answer += 1

    if stack[-1] < y:
        stack.append(y)

    # print(y, stack, answer)

while stack[-1] > 0:
    stack.pop()
    answer += 1

print(answer)
