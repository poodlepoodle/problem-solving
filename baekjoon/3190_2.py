# 백준 3190번: 뱀 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 10^2
N = int(input())

# K <= 10^2
K = int(input())
board = [['' for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().rstrip().split())
    board[r - 1][c - 1] = 'O'

# L <= 10^2
L = int(input())
turns = deque()

for _ in range(L):
    # x <= 10^4
    x, c = input().rstrip().split()
    turns.append((int(x), c))

# 방향 이동 관련
moves = (
    (0, 1), # 우
    (1, 0), # 하
    (0, -1), # 좌
    (-1, 0), # 상
)

# 이동 관련
T = 0
direction = 0
r, c = 0, 0

body = deque()
body.append((0, 0))
board[r][c] = 'h'

# for line in board:
#     print(line)
# print()

while True:
    # 몸길이를 늘려 머리를 다음 칸에 위치시킴
    r, c = body[len(body) - 1]
    dr, dc = moves[direction]
    # print(r, c)

    # 다음 칸이 벽이라면: 종료
    if not(0 <= r + dr < N and 0 <= c + dc < N):
        # print('다음 칸이 벽')
        break

    # 다음 칸이 자신의 몸이라면: 종료
    next_block = board[r + dr][c + dc]
    if next_block == '*':
        # print('다음 칸이 몸')
        break

    body.append((r + dr, c + dc))
    board[r + dr][c + dc] = 'h'
    board[r][c] = '*'
    # 다음 칸에 사과가 있다면:
    if next_block == 'O':
        # 사과는 없어지고 꼬리는 그대로...
        pass
    # 다음 칸에 사과가 없다면:
    else:
        # 꼬리가 위치한 칸을 비워준다
        tail_r, tail_c = body.popleft()
        board[tail_r][tail_c] = ''

    T += 1
    while turns and T == turns[0][0]:
        x, turn = turns.popleft()
        new_d = -1 if turn == 'L' else 1
        direction = (direction + 4 + new_d) % 4

    # for line in board:
    #     print(line)
    # print()

print(T + 1)
