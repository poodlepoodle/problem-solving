# 백준 14502번: 연구소 (2회차)

from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

# N, M <= 8
N, M = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

viruses = []
emptys = []
for r in range(N):
    for c in range(M):
        if maps[r][c] == 2:
            viruses.append((r, c))
            maps[r][c] = 0
        elif maps[r][c] == 0:
            emptys.append((r, c))

moves = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
)

answer = 0
def bfs(additional_walls):
    # print(additional_walls)
    global answer

    # 벽 세우기
    for r, c in additional_walls:
        maps[r][c] = 1

    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    for r, c in viruses:
        q.append((r, c))
        visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < M:
                if maps[r + dr][c + dc] == 0 and not visited[r + dr][c + dc]:
                    q.append((r + dr, c + dc))
                    visited[r + dr][c + dc] = True

    current_answer = 0
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 0 and not visited[r][c]:
                current_answer += 1
    # print(current_answer)
    answer = max(answer, current_answer)

    # 벽 초기화하기
    for r, c in additional_walls:
        maps[r][c] = 0

for additional_walls in combinations(emptys, 3):
    bfs(additional_walls)
print(answer)
