# 백준 15683번: 감시 (2회차)

import sys

input = sys.stdin.readline

# N, M <= 8
N, M = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
watchs = [[0 for _ in range(M)] for _ in range(N)]

# 0은 빈 칸
# 1~5는 CCTV (<= 8개)
# 6은 벽
EMTPY = 0
WALL = 6

cctvs = []
emptys = 0
for r in range(N):
    for c in range(M):
        if maps[r][c] == EMTPY:
            emptys += 1
        elif maps[r][c] < WALL:
            cctvs.append((maps[r][c], r, c))
# for row in maps:
#     print(row)
# print()

# 브루트포싱:
# 1. 8개의 CCTV가 4개 방향 = 4^8 = 2^16 <= 10^5
# 2. 각 CCTV 방향마다 8개 칸
# 10^6 안쪽으로 통과할 것으로 기대
 
directions_per_cctv_types = {
    1: [
        [0],
        [1],
        [2],
        [3]
    ],
    2: [
        [0, 2],
        [1, 3]
    ],
    3: [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0]
    ],
    4: [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 0],
        [3, 0, 1]
    ],
    5: [
        [0, 1, 2, 3]
    ],
}
moves = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < M

def print_maps():
    for r in range(N):
        for c in range(M):
            if watchs[r][c] > 0: print('*', end='')
            elif maps[r][c] == WALL: print('#', end='')
            elif maps[r][c] == EMTPY: print('.', end='')
            else: print(maps[r][c], end='')
        print()
    print()

def bruteforcing(idx):
    # print(f'bruteforcing({idx})')
    global emptys, answer
    
    if idx >= len(cctvs):
        # print(f'---- searched: {emptys} ----')
        # print_maps()
        answer = min(answer, emptys)
        return
    
    cctv_type, cctv_r, cctv_c = cctvs[idx]
    for views in directions_per_cctv_types[cctv_type]:
        # print('views:', views)
        # 각 시야각 별 감시 시작
        for direction in views:
            # print('direction:', direction)
            r, c = cctv_r, cctv_c
            dr, dc = moves[direction]
            while is_valid_position(r + dr, c + dc) and maps[r + dr][c + dc] < WALL:
                r, c = r + dr, c + dc
                if not watchs[r][c] and maps[r][c] == EMTPY:
                    emptys -= 1
                watchs[r][c] += 1
        # 다음 CCTV 브루트포싱
        bruteforcing(idx + 1)
        # 감시 해제
        for direction in views:
            r, c = cctv_r, cctv_c
            dr, dc = moves[direction]
            while is_valid_position(r + dr, c + dc) and maps[r + dr][c + dc] < WALL:
                r, c = r + dr, c + dc
                watchs[r][c] -= 1
                if not watchs[r][c] and maps[r][c] == EMTPY:
                    emptys += 1
    
answer = int(1e9)
bruteforcing(0)
print(answer)
