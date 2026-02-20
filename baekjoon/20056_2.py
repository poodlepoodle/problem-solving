# 백준 20056번: 마법사 상어와 파이어볼 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 50, M <= M^2
# K <= 10^3
N, M, K = map(int, input().rstrip().split())
fireballs = deque()

for _ in range(M):
    r, c, mass, speed, direction = map(int, input().rstrip().split())
    fireballs.append((r - 1, c - 1, mass, speed, direction))
    # print((r - 1, c - 1), ':', (mass, speed, direction))
# print()

# 모든 이동 횟수 -> 10^3
# 이동마다의 파이어볼의 동작
#   1. 모두 각자 이동 -> O(N^2) * 10^3 ~= 10^6 ~ 10^7 -> 이 부분 최적화가 핵심
#   2. 합쳐짐 -> O(N^2) ~= 10^3

moves = {
    0: [-1, 0],
    1: [-1, 1],
    2: [0, 1],
    3: [1, 1],
    4: [1, 0],
    5: [1, -1],
    6: [0, -1],
    7: [-1, -1],
}
maps = [[[] for _ in range(N)] for _ in range(N)]

def print_fireballs():
    for r, c, m, s, d in fireballs:
        print((r, c), ':', (m, s, d))

def fireball_move():
    while fireballs:
        r, c, mass, speed, direction = fireballs.popleft()
        dr, dc = moves[direction]

        new_r, new_c = (r + dr * speed + 1000 * N) % N, (c + dc * speed + 1000 * N) % N
        maps[new_r][new_c].append((mass, speed, direction))

    return maps    

def fireball_merge():
    for r in range(N):
        for c in range(N):
            if len(maps[r][c]) > 1:
                ave_mass = 0
                ave_speed = 0
                ave_direction = [0, 0]
                for mass, speed, direction in maps[r][c]:
                    ave_mass += mass
                    ave_speed += speed
                    ave_direction[direction % 2] += 1

                ave_mass = ave_mass // 5
                if ave_mass == 0:
                    maps[r][c].clear()
                    continue
                
                ave_speed = ave_speed // len(maps[r][c])
                
                next_directions = [0, 2, 4, 6] if ave_direction[0] == 0 or ave_direction[1] == 0 else [1, 3, 5, 7]
                for direction in next_directions:
                    fireballs.append((r, c, ave_mass, ave_speed, direction))
                maps[r][c].clear()
            elif maps[r][c]:
                fireballs.append((r, c, *maps[r][c][0]))
                maps[r][c].clear()

for i in range(K):
    # print(f'{i}th query')
    fireball_move()
    # print('after move:')
    # for r in range(N):
    #     for c in range(N):
    #         if maps[r][c]:
    #             print(f'({r}, {c}):', maps[r][c])
    # print('after merge:')
    fireball_merge()
    # print_fireballs()
    # print('-----------')
    # print()

print(sum([mass for _, _, mass, _, _ in fireballs]))
