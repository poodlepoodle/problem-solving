# 백준 14891번: 톱니바퀴

import sys

input = sys.stdin.readline
gears = [list(map(int, list(input().rstrip()))) for _ in range(4)]
# K <= 10^2
K = int(input())

# 1. 총 K번 회전 -> 10^2
# 2. 각 회전마다 최대 4개까지 톱니바퀴가 따라서 회전 가능 ~= 10
# 결론. 10^5 내에 통과

visited = None
LEFT = 6
RIGHT = 2

def print_gears():
    for gear in gears:
        print(gear)
    print()

def spin(idx, direction):
    # print(f'spin({idx}, {direction})')
    # 왼쪽 기어 체크
    if idx - 1 >= 0 and not visited[idx - 1] and gears[idx - 1][RIGHT] != gears[idx][LEFT]:
        visited[idx - 1] = True
        spin(idx - 1, direction * -1)
    # 오른쪽 기어 체크
    if idx + 1 <= 3 and not visited[idx + 1] and gears[idx][RIGHT] != gears[idx + 1][LEFT]:
        visited[idx + 1] = True
        spin(idx + 1, direction * -1)

    if direction == 1:
        gears[idx] = gears[idx][-1:] + gears[idx][:-1]
    else:
        gears[idx] = gears[idx][1:] + gears[idx][:1]

def get_score():
    score = 0
    for idx in range(4):
        if gears[idx][0]: score += (2 ** idx)
    return score

for _ in range(K):
    gear_idx, gear_direction = map(int, input().rstrip().split())
    # gear_direction: 1이면 시계 방향, -1이면 반시계 방향
    # print(gear_idx, gear_direction)

    visited = [False for _ in range(4)]
    visited[gear_idx - 1] = True
    spin(gear_idx - 1, gear_direction)

    # print_gears()

print(get_score())
