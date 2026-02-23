# 백준 20057번: 마법사 상어와 토네이도 (2회차)

import sys

input = sys.stdin.readline

# N <= 499
N = int(input())
sands = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 시간복잡도 자체는...
#   1. 격자의 모든 칸에 대해서 모래 날리기 -> O(N^2) ~= 10^5
#   2. 각 칸마다 날라간 모래 계산 ~= 10
#   결론: 시간복잡도 때문에 문제 생길 것 같지는 않음

moves = [
    [0, -1], # <
    [1, 0], # v
    [0, 1], # >
    [-1, 0], # ^
]

splits = [
    [
        [-1, 0, 0.01],
        [1, 0, 0.01],
        [-1, -1, 0.07],
        [1, -1, 0.07],
        [-2, -1, 0.02],
        [2, -1, 0.02],
        [-1, -2, 0.1],
        [1, -2, 0.1],
        [0, -3, 0.05],
    ],
    [
        [0, -1, 0.01],
        [0, 1, 0.01],
        [1, -1, 0.07],
        [1, 1, 0.07],
        [1, -2, 0.02],
        [1, 2, 0.02],
        [2, -1, 0.1],
        [2, 1, 0.1],
        [3, 0, 0.05],
    ],
    [
        [-1, 0, 0.01],
        [1, 0, 0.01],
        [-1, 1, 0.07],
        [1, 1, 0.07],
        [-2, 1, 0.02],
        [2, 1, 0.02],
        [-1, 2, 0.1],
        [1, 2, 0.1],
        [0, 3, 0.05],
    ],
    [
        [0, -1, 0.01],
        [0, 1, 0.01],
        [-1, -1, 0.07],
        [-1, 1, 0.07],
        [-1, -2, 0.02],
        [-1, 2, 0.02],
        [-2, -1, 0.1],
        [-2, 1, 0.1],
        [-3, 0, 0.05],
    ],
]

remains = [
    [0, -2],
    [2, 0],
    [0, 2],
    [-2, 0]
]

r, c = N // 2, N // 2
direction = 0
answer = 0

def is_in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def print_sands(current_r, current_c):
    global answer
    for r in range(N):
        for c in range(N):
            if r == current_r and c == current_c: print('#', end=' ')
            elif not sands[r][c]: print('.', end=' ')
            else: print(sands[r][c], end=' ')
        print()
    print(f'answer: {answer}')
    print()

def split(r, c, direction):
    global answer
    # print(f'split(r: {r}, c: {c}), direction: {direction}')

    # y칸의 좌표 저장
    dr, dc = moves[direction]
    yr, yc = r + dr, c + dc
    y_sands = sands[yr][yc]
    if not y_sands: return
    
    for dr, dc, portion in splits[direction]:
        # 이동할 모래의 양 계산, 소수점 아래 버림
        z_sands = int(y_sands * portion)
        # 모래의 이동
        sands[yr][yc] -= z_sands
        if is_in_board(r + dr, c + dc):
            sands[r + dr][c + dc] += z_sands
        else:
            answer += z_sands

    dr, dc = remains[direction]
    ar, ac = r + dr, c + dc
    if is_in_board(ar, ac):
        sands[ar][ac] += sands[yr][yc]
    else:
        answer += sands[yr][yc]
    sands[yr][yc] = 0

for i in range(1, N):
    for _ in range(i):
        split(r, c, direction)
        # print_sands(r, c)
        dr, dc = moves[direction]
        r, c = r + dr, c + dc
    direction = (direction + 1) % 4
    for _ in range(i):
        split(r, c, direction)
        # print_sands(r, c)
        dr, dc = moves[direction]
        r, c = r + dr, c + dc
    direction = (direction + 1) % 4
for _ in range(i):
    split(r, c, direction)
    # print_sands(r, c)
    dr, dc = moves[direction]
    r, c = r + dr, c + dc
direction = (direction + 1) % 4

print(answer)
