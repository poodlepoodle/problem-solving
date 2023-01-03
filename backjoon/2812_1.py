from collections import deque
import sys

input = sys.stdin.readline

# 최대 5 * 10^5
N, K = map(int, input().rstrip().split())

digits = deque(input().rstrip())

q = deque()
q.append(digits.popleft())
k = K

while digits:
    digit = digits.popleft()

    while k and q and q[-1] < digit:
        q.pop()
        k -= 1
    
    q.append(digit)
    # print(q)

print(int("".join(list(q)[:(N - K)])))
