import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

subin, sister = map(int, input().split())

# 1차원 BFS의 탐색 횟수는 최대 10^5 정도~

visited = [False] * 100001

q = deque()
q.append((0, subin))

answer = 100000
ways = 0

while q:
    level, subin = q.popleft()

    if level > answer:
        break

    if subin == sister:
        answer = level
        ways += 1
        continue

    visited[subin] = True

    next_moves = ((subin + 1), (subin - 1), (subin * 2))

    for next_subin in next_moves:
        if 0 <= next_subin <= 100000 and not visited[next_subin]:
            q.append((level + 1, next_subin))

print(answer)
print(ways)
