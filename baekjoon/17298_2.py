# 백준 17298번: 오큰수 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 10^6
N = int(input())
array = list(map(int, input().rstrip().split()))

# 전략
# 1. N이 최대 10^6이므로 O(N) 혹은 최대 O(NlogN)이어야 함
# 2. 스택을 이용하면 좋을 것 같은 느낌? (백준 스카이라인과 유사)
# 3. 설명에서 '그러한 수가 없는 경우 오큰수는 -1' -> 스택이 비었을 때일 것 같은 느낌?
# 4. 스택을 앞 혹은 뒤에서부터 할지만 결정하면 될 듯

stack = []
answer = deque()

for idx in range(len(array) - 1, -1, -1):
    number = array[idx]

    while stack and stack[-1] <= number:
        stack.pop()

    if len(stack) == 0:
        answer.appendleft(-1)
    else:
        answer.appendleft(stack[-1])
    stack.append(number)

print(" ".join(map(str, answer)))
