# 백준 18405번: 경쟁적 전염

from collections import deque
import sys

input = sys.stdin.readline

# N <= 10^2, K <= 10^3
N, K = map(int, input().rstrip().split())

viruses = []
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if maps[r][c] != 0:
            viruses.append((maps[r][c], r, c))
viruses.sort(key=lambda x:x[0])

q = deque()
for type, r, c in viruses:
    q.append((1, type, r, c))

moves = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)
# S <= 10^4, X, Y <= 10^2
S, X, Y = map(int, input().rstrip().split())

while q:
    time, type, r, c = q.popleft()

    if time > S: break

    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < N:
            if maps[r + dr][c + dc] == 0:
                maps[r + dr][c + dc] = type
                q.append((time + 1, type, r + dr, c + dc))

    # for row in maps:
    #     print(row)
    # print()

print(maps[X - 1][Y - 1])
