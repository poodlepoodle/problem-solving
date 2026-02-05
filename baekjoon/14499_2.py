# 백준 14499번: 주사위 굴리기 (2회차)

import sys

input = sys.stdin.readline

# 보드의 크기 N, M <= 20
# 명령의 개수 K <= 10^3
N, M, X, Y, K = map(int, input().rstrip().split())

# 10^3개의 쿼리마다 각 이동 명령은 O(1)에 처리 가능할 것으로 예상...

maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

dice = {
    'top': 0,
    'bottom': 0,
    'front': 0,
    'back': 0,
    'left': 0,
    'right': 0
}

directions = {
    'front': (-1, 0),
    'back': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command_to_direction = {
    1: 'right',
    2: 'left',
    3: 'front',
    4: 'back',
}

def dice_move(move_direction):
    if move_direction == 'front':
        dice['top'], dice['front'], dice['bottom'], dice['back'] = dice['back'], dice['top'], dice['front'], dice['bottom']
    elif move_direction == 'back':
        dice['back'], dice['bottom'], dice['front'], dice['top'] = dice['top'], dice['back'], dice['bottom'], dice['front']
    elif move_direction == 'left':
        dice['top'], dice['left'], dice['bottom'], dice['right'] = dice['right'], dice['top'], dice['left'], dice['bottom']
    elif move_direction == 'right':
        dice['top'], dice['right'], dice['bottom'], dice['left'] = dice['left'], dice['top'], dice['right'], dice['bottom']

r, c = X, Y
queries = list(map(int, input().rstrip().split()))

for command in queries:
    # print('command:', command)
    direction = command_to_direction[command]
    dr, dc = directions[direction]

    if not(0 <= r + dr < N and 0 <= c + dc < M): continue

    r, c = r + dr, c + dc
    dice_move(direction)

    if maps[r][c] == 0:
        maps[r][c] = dice['bottom']
    else:
        dice['bottom'], maps[r][c] = maps[r][c], 0

    print(dice['top'])
