# 백준 2812번: 크게 만들기 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N, K <= 5 * 10^5
N, K = map(int, input().rstrip().split())

original = deque(list(input().rstrip()))

q = deque()
k = K
q.append(original.popleft())
# print(q)

while original and k:
    digit = original.popleft()
    # print(f"{digit}, K: {k}")

    while q and (q[-1] < digit) and (len(q) + len(original) >= N - K):
        # print(len(q), len(original), N - K)
        k -= 1
        q.pop()
    
    if len(q) < N - K:
        q.append(digit)
    # print(q)

while len(q) < N - K and original:
    q.append(original.popleft())

print("".join(q))
