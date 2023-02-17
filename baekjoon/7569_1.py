import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())

# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((0, i, j, k))
                visited[i][j][k] = True

directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

days = 0

while q:
    current, l, r, c = q.popleft()

    if days < current:
        days = current

    for dl, dr, dc in directions:
        new_l, new_r, new_c = l + dl, r + dr, c + dc

        if 0 <= new_l < H and 0 <= new_r < N and 0 <= new_c < M:
            if box[new_l][new_r][new_c] == 0 and not visited[new_l][new_r][new_c]:
                q.append((current + 1, new_l, new_r, new_c))
                visited[new_l][new_r][new_c] = True

remain = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0 and not visited[i][j][k]:
                print(-1)
                exit()
print(days)
