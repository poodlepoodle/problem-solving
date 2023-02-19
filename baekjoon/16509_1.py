from collections import deque
import sys

input = sys.stdin.readline

sang_r, sang_c = map(int, input().rstrip().split())
wang_r, wang_c = map(int, input().rstrip().split())

q = deque()
visited = [[False for _ in range(9)] for _ in range(10)]

q.append((sang_r, sang_c, 0))
visited[sang_r][sang_c] = True

paths = (((-1, 0), (-2, -1), (-3, -2)),\
    ((-1, 0), (-2, 1), (-3, 2)),\
    ((0, 1), (-1, 2), (-2, 3)),\
    ((0, 1), (1, 2), (2, 3)),\
    ((1, 0), (2, -1), (3, -2)),\
    ((1, 0), (2, 1), (3, 2)),\
    ((0, -1), (-1, -2), (-2, -3)),\
    ((0, -1), (1, -2), (2, -3)))

answer = -1

while q:
    r, c, level = q.popleft()

    if r == wang_r and c == wang_c:
        answer = level
        break

    for path in paths:
        cnt = 0
        for dr, dc in path[:2]:
            if (0 <= r + dr < 10) and (0 <= c + dc < 9) and not (r + dr == wang_r and c + dc == wang_c):
                cnt += 1
            else:
                break
        # print(cnt)
        if cnt == 2:
            dr, dc = path[2]
            if 0 <= r + dr < 10 and 0 <= c + dc < 9:
                if not visited[r + dr][c + dc]:
                    visited[r + dr][c + dc] = True
                    q.append((r + dr, c + dc, level + 1))
    # print(q)
    # print()

print(answer)
