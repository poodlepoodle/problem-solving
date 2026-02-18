# 백준 17144번: 미세먼지 안녕! (3회차)

import sys

input = sys.stdin.readline

# R, C <= 50
# T <= 10^3
R, C, T = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(R)]

EMPTY = 0
CLEANER = -1

cleaner_r_top, cleaner_r_bottom = -1, -1
for r in range(R):
    if maps[r][0] == CLEANER:
        cleaner_r_top, cleaner_r_bottom = r, r + 1
        break

# 1초 동안 일어나는 일
#   1. 확산: 모든 칸마다 4개 방향 -> 4 * 50 * 50 <= 10^4
#   2. 순환: 최대 모든 칸 < 10^4
# 주어진 시간은 T초 < 10^3
# 예상: 10^7~10^8 이내

moves = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

def is_empty(r, c):
    return maps[r][c] == EMPTY

def is_cleaner(r, c):
    return (cleaner_r_top <= r <= cleaner_r_bottom) and c == 0

def is_in_board(r, c):
    return 0 <= r < R and 0 <= c < C

def print_board():
    for row in maps:
        print(row)
    print()

def diffusion():
    diffused_maps = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if is_cleaner(r, c): continue
            if is_empty(r, c): continue

            diffused_maps[r][c] += maps[r][c]
            unit_diffusion = maps[r][c] // 5
            for dr, dc in moves:
                if is_in_board(r + dr, c + dc) and not is_cleaner(r + dr, c + dc):
                    diffused_maps[r + dr][c + dc] += unit_diffusion
                    diffused_maps[r][c] -= unit_diffusion

    diffused_maps[cleaner_r_top][0], diffused_maps[cleaner_r_bottom][0] = -1, -1
    return diffused_maps

def circulation():
    # upper circulation
    for r in range(cleaner_r_top - 1, 0, -1):
        maps[r][0] = maps[r - 1][0]
    for c in range(C - 1):
        maps[0][c] = maps[0][c + 1]
    for r in range(cleaner_r_top):
        maps[r][C - 1] = maps[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        maps[cleaner_r_top][c] = maps[cleaner_r_top][c - 1]
    maps[cleaner_r_top][1] = 0

    # lower circulation
    for r in range(cleaner_r_bottom + 1, R - 1):
        maps[r][0] = maps[r + 1][0]
    for c in range(C - 1):
        maps[R - 1][c] = maps[R - 1][c + 1]
    for r in range(R - 1, cleaner_r_bottom, -1):
        maps[r][C - 1] = maps[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        maps[cleaner_r_bottom][c] = maps[cleaner_r_bottom][c - 1]
    maps[cleaner_r_bottom][1] = 0

def count_dusts():
    cnt = 0
    for r in range(R):
        for c in range(C):
            if not is_cleaner(r, c):
                cnt += maps[r][c]
    return cnt

for _ in range(T):
    maps = diffusion()
    # print_board()
    circulation()
    # print_board()
    # print('------------')

print(count_dusts())
