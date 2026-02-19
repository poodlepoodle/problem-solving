# 백준 17142번: 연구소 3 (3회차)

from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

# N <= 50
# M <= 10
N, M = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

EMPTY = 0
WALL = 1
VIRUS = 2
NOT_VISITED = -1

total_viruses = []
for r in range(N):
    for c in range(N):
        if maps[r][c] == VIRUS: total_viruses.append((r, c))

# 바이러스 조합
#   10개 중 M개 선택 -> 10CM <= 10C5 = 252 < 10^3
# 각 조합마다 바이러스 퍼지는 시뮬레이션
#   모든 칸에 대한 BFS -> O(N^2) = 2500 < 10^4
# 결론: 10^3 * 10^4 < 10^8

moves = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

def is_in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def print_visited(visited):
    print('#-------#')
    for r in range(N):
        for c in range(N):
            if maps[r][c] == WALL: print('-', end=' ')
            elif visited[r][c] == NOT_VISITED:
                if maps[r][c] == VIRUS: print('*', end=' ')
                else: print('-', end=' ')
            else: print(visited[r][c], end=' ')
        print()
    print('#-------#')
    print()

def bfs(viruses):
    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    moved_max = 0

    for vr, vc in viruses:
        q.append((vr, vc, 0))
        visited[vr][vc] = 0

    while q:
        r, c, moved = q.popleft()
        if maps[r][c] == EMPTY:
            moved_max = max(moved_max, moved)

        for dr, dc in moves:
            if is_in_board(r + dr, c + dc):
                if maps[r + dr][c + dc] != WALL and visited[r + dr][c + dc] == NOT_VISITED:
                    q.append((r + dr, c + dc, moved + 1))
                    visited[r + dr][c + dc] = moved + 1
    
    # print_visited(visited)

    for r in range(N):
        for c in range(N):
            if maps[r][c] == EMPTY and visited[r][c] == NOT_VISITED: return -1
    
    return moved_max

answer = int(1e9)
for viruses in combinations(total_viruses, M):
    current_answer = bfs(viruses)
    if current_answer != -1:
        answer = min(answer, current_answer)

print(answer if answer != int(1e9) else -1)
