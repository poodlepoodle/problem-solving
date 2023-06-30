# 백준 20057번: 마법사 상어와 토네이도

import sys

input = sys.stdin.readline

# N <= 5 * 10^2
N = int(input())

sands = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 왼쪽, 아래, 오른쪽, 위 = 0, 1, 2, 3
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

moves = {
    # 왼쪽
    0: {
        1: ((-1, 1), (1, 1)),
        2: ((-2, 0), (2, 0)),
        5: [(0, -2)],
        7: ((-1, 0), (1, 0)),
        10: ((-1, -1), (1, -1))
    },
    # 아래
    1: {
        1: ((-1, -1), (-1, 1)),
        2: ((0, -2), (0, 2)),
        5: [(2, 0)],
        7: ((0, -1), (0, 1)),
        10: ((1, -1), (1, 1)),
    },
    # 오른쪽
    2: {
        1: ((-1, -1), (1, -1)),
        2: ((-2, 0), (2, 0)),
        5: [(0, 2)],
        7: ((-1, 0), (1, 0)),
        10: ((-1, 1), (1, 1))
    },
    # 위
    3: {
        1: ((1, -1), (1, 1)),
        2: ((0, -2), (0, 2)),
        5: [(-2, 0)],
        7: ((0, -1), (0, 1)),
        10: ((-1, -1), (-1, 1)),
    },
}

tor_r, tor_c = [N // 2] * 2
tor_direction = 0
big_step = 1
small_step = 0
repeat = True
answer = 0

while tor_r != 0 or tor_c != 0:
    small_step += 1
    # print(big_step, small_step, tor_direction)

    next_dr, next_dc = directions[tor_direction]
    tor_r, tor_c = tor_r + next_dr, tor_c + next_dc
    current_sand = sands[tor_r][tor_c]

    for percent, drdcs in moves[tor_direction].items():
        # print(drdcs)
        for dr, dc in drdcs:
            if 0 <= tor_r + dr < N and 0 <= tor_c + dc < N:
                sands[tor_r + dr][tor_c + dc] += int(current_sand * percent / 100)
            else:
                answer += int(current_sand * percent / 100)
            sands[tor_r][tor_c] -= int(current_sand * percent / 100)
    
    if 0 <= tor_r + next_dr < N and 0 <= tor_c + next_dc < N:
        sands[tor_r + next_dr][tor_c + next_dc] += sands[tor_r][tor_c]
    else:
        answer += sands[tor_r][tor_c]
    sands[tor_r][tor_c] = 0

    # for row in sands:
    #     print(row)
    # print()

    if big_step == small_step:
        if repeat:
            repeat = False
            small_step = 0
        else:
            repeat = True
            big_step += 1
            small_step = 0
        tor_direction = (tor_direction + 1) % 4

print(answer)
