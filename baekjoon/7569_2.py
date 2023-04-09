from collections import deque
import sys

input = sys.stdin.readline

# M, N, H <= 10^2
M, N, H = map(int, input().rstrip().split())

box = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

q = deque()

for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                visited[h][r][c] = True
                q.append((h, r, c, 0))

moves = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))

answer = -1

while q:
    h, r, c, day = q.popleft()

    answer = max(answer, day)

    for dh, dr, dc in moves:
        if 0 <= h + dh < H and 0 <= r + dr < N and 0 <= c + dc < M:
            if box[h + dh][r + dr][c + dc] == 0 and not visited[h + dh][r + dr][c + dc]:
                visited[h + dh][r + dr][c + dc] = True
                q.append((h + dh, r + dr, c + dc, day + 1))
    
    # print(q)

all_riped = True

for h in range(H):
    for r in range(N):
        for c in range(M):
            if not box[h][r][c] and not visited[h][r][c]:
                all_riped = False

print(answer if all_riped else -1)
