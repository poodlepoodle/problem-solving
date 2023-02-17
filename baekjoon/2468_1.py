from collections import deque
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 최대 10^2
N = int(input())

area = [list(map(int, input().rstrip().split())) for _ in range(N)]
max_level = max([max(row) for row in area])

# 한번 dfs 조사: 10^4
# 모든 강수 레벨에 대해 검사: 10^2
# -> 해볼 만 함

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

# def dfs(r, c, level):
#     for dr, dc in moves:
#         if 0 <= r + dr < N and 0 <= c + dc < N:
#             if not visited[r + dr][c + dc] and area[r + dr][c + dc] > level:
#                 visited[r + dr][c + dc] = True
#                 dfs(r + dr, c + dc, level)

def bfs(r, c, level):
    q = deque()
    visited[r][c] = True
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if not visited[r + dr][c + dc] and area[r + dr][c + dc] > level:
                    visited[r + dr][c + dc] = True
                    q.append((r + dr, c + dc))

max_safe_area = 0

for level in range(0, max_level):
    visited = [[False for _ in range(N)] for _ in range(N)]

    safe_area = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > level:
                visited[i][j] = True
                # dfs(i, j, level)
                bfs(i, j, level)
                safe_area += 1

    # print(safe_area)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
