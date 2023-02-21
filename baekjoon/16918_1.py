import sys

input = sys.stdin.readline

# R, C, N <= 2 * 10^2
R, C, N = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(R)]
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 모든 칸을 한 번 순회 -> 4 * 10^4
# 최대 지날 수 있는 시간 -> 2 * 10^2
# 모든 칸에 대해서 반복해도 10^7 정도이므로 시간 초과되지 않고 통과할 수 있을 것으로 기대함

T = 1
mark = True

for r in range(R):
    for c in range(C):
        if board[r][c] == 'O':
            board[r][c] = mark


# for row in board:
#     print(row)
# print()

# 0~1초 : 초기 상태
# 2초 : 나머지 칸에 폭탄 설치
# 3초 : 미리 설치한 폭탄 폭발
# 4초 : 나머지 칸에 폭탄 설치
# 5초 : 미리 설치한 폭탄 폭발
# 6초 : ...

while T <= N:
    if T <= 1:
        T += 1
        continue

    if T % 2 == 0: # 나머지 칸에 폭탄 설치
        for r in range(R):
            for c in range(C):
                if board[r][c] != mark:
                    board[r][c] = (not mark)
    else: # 미리 설치한 폭탄 폭발
        booms = []
        for r in range(R):
            for c in range(C):
                if board[r][c] == mark:
                    booms.append((r, c))
                    for dr, dc in directions:
                        if 0 <= r + dr < R and 0 <= c + dc < C:
                            booms.append((r + dr, c + dc))
        for r, c in booms:
            board[r][c] = '.'
        mark = (not mark)

    T += 1

    # for row in board:
    #     print(row)
    # print()

if T % 2 == 0:
    for r in range(R):
        for c in range(C):
            if board[r][c] == mark:
                board[r][c] = 'O'
else:
    for r in range(R):
        for c in range(C):
            board[r][c] = 'O'

for row in board:
    print("".join(row))
