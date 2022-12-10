from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 0은 빈 칸, 1은 벽, 2는 바이러스
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

available_walls = []
viruses = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            available_walls.append((i, j))
        elif maps[i][j] == 2:
            maps[i][j] = 0
            viruses.append((i, j))

# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 꼭 "3개" ?

# (3 ≤ N, M ≤ 8)
# 한번 BFS 돌리는 데 N * M = 16

# 벽을 3개 정하는 갯수 : 16C3 = 16 15 14 / 3 2 = 16 * 5 * 7 <= 10^3
# 최대 10^3개만큼 벽을 3개 정한 후에 한번씩 BFS 돌려봐도 될듯...

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(walls):
    current_maps = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            current_maps[i][j] = maps[i][j]
    for r, c in walls:
        current_maps[r][c] = 1

    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    for r, c in viruses:
        q.append((r, c))
        visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < M:
                if current_maps[r + dr][c + dc] == 0 and not visited[r + dr][c + dc]:
                    q.append((r + dr, c + dc))
                    visited[r + dr][c + dc] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if current_maps[i][j] == 0 and not visited[i][j]:
                cnt += 1
    
    return cnt

# 벽을 3개 정하는 경우의 수
max_safes = 0
for walls in combinations(available_walls, 3):
    safes = bfs(walls)
    max_safes = max(max_safes, safes)

print(max_safes)
