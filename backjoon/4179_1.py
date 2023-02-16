from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

maps = [list(input().rstrip()) for _ in range(R)]

q = deque()
visited = [[2001 for _ in range(C)] for _ in range(R)]

jr, jc = -1, -1

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'J':
            jr, jc = i, j
        elif maps[i][j] == 'F':
            q.append((i, j, 0))
            visited[i][j] = 0

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

while q:
    r, c, times = q.popleft()

    for dr, dc in moves:
        # print(r + dr, c + dc)
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if maps[r + dr][c + dc] != '#':
                if visited[r + dr][c + dc] > times + 1:
                    visited[r + dr][c + dc] = times + 1
                    q.append((r + dr, c + dc, times + 1))

                    # print(q)
    # print(q)

q = deque([(jr, jc, 0)])
answer = -1

# for row in visited:
#     print(row)
# print()

while q:
    jr, jc, times = q.popleft()

    if jr == 0 or jr == R - 1 or jc == 0 or jc == C - 1:
        answer = times + 1
        break

    for dr, dc in moves:
        if 0 <= jr + dr < R and 0 <= jc + dc < C:
            if maps[jr + dr][jc + dc] != '#':
                if visited[jr + dr][jc + dc] > times + 1:
                    visited[jr + dr][jc + dc] = times + 1
                    q.append((jr + dr, jc + dc, times + 1))

    # print(q)

print(answer if answer != -1 else 'IMPOSSIBLE')
