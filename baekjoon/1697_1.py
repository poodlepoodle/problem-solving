import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

q = deque()
visited = [False] * 100001

q.append((0, N))
visited[N] = True
answer = -1

while q:
    level, subin = q.popleft()

    if subin == K:
        answer = level
        break

    if 0 <= subin - 1 and not visited[subin - 1]:
        q.append((level + 1, subin - 1))
        visited[subin - 1] = True
    if subin + 1 <= 100000 and not visited[subin + 1]:
        q.append((level + 1, subin + 1))
        visited[subin + 1] = True
    if subin * 2 <= 100000 and not visited[subin * 2]:
        q.append((level + 1, subin * 2))
        visited[subin * 2] = True

print(answer)
