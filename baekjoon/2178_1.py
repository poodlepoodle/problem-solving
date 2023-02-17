import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, 1)])
visited[0][0] = True

moves = ((0, 1), (1, 0), (-1, 0), (0, -1))

answer = 0
while q:
    r, c, level = q.popleft()

    if r == N - 1 and c == M - 1:
        answer = level
        break

    for dr, dc in moves:
        next_r, next_c = r + dr, c + dc
        if 0 <= next_r < N and 0 <= next_c < M:
            if maze[next_r][next_c] == 1 and not visited[next_r][next_c]:
                q.append((next_r, next_c, level + 1))
                visited[next_r][next_c] = True

print(answer)
