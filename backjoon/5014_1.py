import sys

def input(): return sys.stdin.readline().rstrip()

Floors, Start, Goal, Up, Down = map(int, input().split())

# 모든 층의 갯수 F : 최대 10^6
# 최소 횟수로 목표 층에 도달하는 방법을 체크해야 하므로 BFS 수행

from collections import deque

q = deque()
visited = [False] * (Floors + 1)

q.append((0, Start))
visited[0] = True

answer = 'use the stairs'
while q:
    count, current = q.popleft()

    if current == Goal:
        answer = count
        break

    if current + Up <= Floors and not visited[current + Up]:
        q.append((count + 1, current + Up))
        visited[current + Up] = True
    if current - Down > 0 and not visited[current - Down]:
        q.append((count + 1, current - Down))
        visited[current - Down] = True

print(answer)
