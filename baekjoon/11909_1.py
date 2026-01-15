# 백준 11909번: 배열 탈출

import sys

input = sys.stdin.readline

# N <= 2222 ~= 10^3
N = int(input())
maze = [list(map(int, input().rstrip().split())) for _ in range(N)]

visited = [[float('inf') for _ in range(N)] for _ in range(N)]
visited[0][0] = 0

prev_moves = (
    (-1, 0),
    (0, -1)
)

for r in range(N):
    for c in range(N):
        if r == 0 and c == 0: continue
        # print(r, c)

        for dr, dc in prev_moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                cost = -maze[r + dr][c + dc] + maze[r][c] + 1 if maze[r + dr][c + dc] <= maze[r][c] else 0
                visited[r][c] = min(visited[r][c], visited[r + dr][c + dc] + cost)

    # for row in visited:
    #     print(row)
    # print()

print(visited[-1][-1])
