# 백준 2206번: 벽 부수고 이동하기 (3회차)

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]

start_r, start_c = 0, 0
end_r, end_c = N - 1, M - 1

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

q = deque()
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

q.append((0, start_r, start_c, 1))
visited[0][start_r][start_c] = 1

answer = int(1e9)

while q:
    breaked, r, c, dist = q.popleft()

    if r == end_r and c == end_c:
        answer = min(answer, dist)

    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            if maps[r + dr][c + dc] == 0 and not visited[breaked][r + dr][c + dc]:
                visited[breaked][r + dr][c + dc] = dist + 1
                q.append((breaked, r + dr, c + dc, dist + 1))
            elif maps[r + dr][c + dc] and not breaked and not visited[1][r + dr][c + dc]:
                visited[1][r + dr][c + dc] = dist + 1
                q.append((1, r + dr, c + dc, dist + 1))

print(-1 if answer == int(1e9) else answer)
