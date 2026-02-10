# 백준 14503번: 로봇 청소기 (3회차)

import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
cleaned = [[False for _ in range(M)] for _ in range(N)]

moves = (
    (-1, 0), # 북
    (0, 1), # 동
    (1, 0), # 남
    (0, -1), # 서
)

def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < M

def is_empty_and_not_cleaned(r, c):
    return maps[r][c] == 0 and not cleaned[r][c]

def is_all_cleaned_arounds(r, c):
    for dr, dc in moves:
        if is_valid_position(r + dr, c + dc):
            if is_empty_and_not_cleaned(r + dr, c + dc):
                return False
    return True

def can_go_back(r, c, d):
    dr, dc = moves[(d + 2) % 4]
    if is_valid_position(r + dr, c + dc):
        if maps[r + dr][c + dc] == 0:
            return True
    return False

answer = 0
while True:
    # print(r, c, d)
    # for row in range(N):
    #     for col in range(M):
    #         if r == row and c == col:
    #             print('*', end= ' ')
    #         elif maps[row][col] == 0 and cleaned[row][col]:
    #             print('2', end= ' ')
    #         else:
    #             print(maps[row][col], end= ' ')
    #     print()

    # 현재 칸이 청소되지 않은 경우 청소
    if is_empty_and_not_cleaned(r, c):
        answer += 1
        # print('answer:', answer)
        cleaned[r][c] = True
    # print()

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이
    #   없는 경우
    if is_all_cleaned_arounds(r, c):
        # 바라보는 방향 그대로 한 칸 후진 가능하면
        if can_go_back(r, c, d):
            # 한 칸 후진하고 다시 1번으로...
            dr, dc = moves[(d + 2) % 4]
            r, c = r + dr, c + dc
            continue
        # 후진 불가능하면
        else:
            # 작동 멈춤
            break
    #   있는 경우
    else:
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4
        # 바라보는 방향 기준 앞쪽이 청소되지 않은 빈칸인 경우 한칸 전진
        dr, dc = moves[d]
        if is_empty_and_not_cleaned(r + dr, c + dc):
            r, c = r + dr, c + dc
        continue

print(answer)
