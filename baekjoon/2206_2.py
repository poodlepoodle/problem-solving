# 백준 2206번: 벽 부수고 이동하기 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N, M <= 10^3
N, M = map(int, input().rstrip().split())

maps = [list(input().rstrip()) for _ in range(N)]

# visited[0][i][j]: 벽이 깨지지 않은 상태에서 (i, j)에 방문 여부
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

q = deque([(0, 0, 1, 0)])
visited[0][0][0] = 1

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

answer = -1

while q:
    r, c, cnt, breaked = q.popleft()

    if r == N - 1 and c == M - 1:
        answer = cnt
        break

    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            # 벽이 아닌 경우: 부술 필요 없이 그냥 통과하면 됨
            if maps[r + dr][c + dc] == '0':
                if not visited[breaked][r + dr][c + dc]:
                    q.append((r + dr, c + dc, cnt + 1, breaked))
                    visited[breaked][r + dr][c + dc] = cnt + 1
            # 벽인데 부술 수 있는 경우: 
            elif not breaked:
                if not visited[1][r + dr][c + dc]:
                    q.append((r + dr, c + dc, cnt + 1, 1))
                    visited[1][r + dr][c + dc] = cnt + 1

print(answer)
