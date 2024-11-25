# 백준 1926번: 그림

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
pics_cnt = 0
max_pic_size = 0

def bfs(start_r, start_c):
    global visited
    q = deque()
    visited_cnt = 0

    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    visited_cnt += 1

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            if 0 <= r + dr < N and 0 <= c + dc < M:
                if board[r + dr][c + dc] == 1 and not visited[r + dr][c + dc]:
                    q.append((r + dr, c + dc))
                    visited[r + dr][c + dc] = True
                    visited_cnt += 1

    return visited_cnt

for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and not visited[r][c]:
            pics_cnt += 1
            max_pic_size = max(max_pic_size, bfs(r, c))

print(pics_cnt)
print(max_pic_size)
