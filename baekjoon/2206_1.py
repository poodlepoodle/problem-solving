from collections import deque
import sys

input = sys.stdin.readline

# N, M <= 10^3
N, M = map(int, input().rstrip().split())

# 0은 빈 칸, 1은 벽
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 시작점은 (0, 0), 도착점은 (N - 1, M - 1)
q = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

q.append((0, 0, 1, 0))
visited[0][0][0] = True

answer = -1

while q:
    r, c, level, breaked = q.popleft()

    if (r == N - 1) and (c == M - 1):
        answer = level
        break

    for dr, dc in moves:
        if (0 <= r + dr < N) and (0 <= c + dc < M):
            if maps[r + dr][c + dc] == 1:
                if not breaked:
                    visited[1][r + dr][c + dc] = True
                    q.append((r + dr, c + dc, level + 1, 1))
            else:
                if not visited[breaked][r + dr][c + dc]:
                    visited[breaked][r + dr][c + dc] = True
                    q.append((r + dr, c + dc, level + 1, breaked))

print(answer)
