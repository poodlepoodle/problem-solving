from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

maps = [list(input()) for _ in range(N)]
islands = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            islands.append((i, j))

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs(r, c):
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    q.append((r, c, 0))
    visited[r][c] = True

    distance = 0
    while q:
        r, c, depth = q.popleft()

        distance = max(distance, depth)

        for dr, dc in moves:
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < N and 0 <= next_c < M:
                if maps[next_r][next_c] == 'L' and not visited[next_r][next_c]:
                    q.append((next_r, next_c, depth + 1))
                    visited[next_r][next_c] = True

    return distance

max_distance = 0
for r, c in islands:
    # print(f"{r}, {c} -> ", end='')
    
    distance = bfs(r, c)
    # print(distance, end = ' -> ')

    max_distance = max(max_distance, distance)
    # print(max_distance)

print(max_distance)
