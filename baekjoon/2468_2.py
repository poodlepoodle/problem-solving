# 백준 2468반: 안전 영역 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

N = int(input()) # N < 10^2
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

# 모든 높이에 대해서 조사하다면 -> 10^2
# 각 높이에 대해서 dfs를 수행한다면 -> 10^4
# 10^6으로 돌려볼만 함

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(r, c, rain, visited):
    q = deque()

    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if maps[r + dr][c + dc] > rain and not visited[r + dr][c + dc]:
                    visited[r + dr][c + dc] = True
                    q.append((r + dr, c + dc))

answer = 0

for rain in range(100):
    for r in range(N):
        for c in range(N):
            visited[r][c] = False
    current_answer = 0

    for r in range(N):
        for c in range(N):
            if maps[r][c] > rain and not visited[r][c]:
                bfs(r, c, rain, visited)
                current_answer += 1
    
    # 모든 지역에 대해서 돌고 나서 
    answer = max(answer, current_answer)

print(answer)
