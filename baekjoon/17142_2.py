# 백준 17142번: 연구소 3

from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

# N <= 50, M <= 10
N, M = map(int, input().rstrip().split())

# 0은 빈 칸, 1은 벽, 2는 바이러스의 위치
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

viruses = []
for r in range(N):
    for c in range(N):
        if maps[r][c] == 2:
            viruses.append((r, c))

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

answer = int(1e9)
for virus in combinations(viruses, M):
    # print(virus)
    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for r, c in virus:
        q.append((r, c, 0))
        visited[r][c] = 0

    while q:
        r, c, depth = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                # 벽이 아니고 아직 방문하지 않은 경우
                if maps[r + dr][c + dc] != 1 and visited[r + dr][c + dc] == -1:
                    q.append((r + dr, c + dc, depth + 1))
                    visited[r + dr][c + dc] = depth + 1
    
    current_answer = 0
    wrong_answer = False
    for r in range(N):
        for c in range(N):
            if maps[r][c] == 0 and visited[r][c] == -1:
                wrong_answer = True
            
            if (r, c) not in viruses:
                current_answer = max(current_answer, visited[r][c])

    if not wrong_answer:
        answer = min(answer, current_answer)

    # print(current_answer)
    # print(wrong_answer)
    # for row in visited:
    #     print(*row)
    # print()

print(answer if answer != int(1e9) else -1)
