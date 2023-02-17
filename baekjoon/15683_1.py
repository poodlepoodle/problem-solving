from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 전체 칸 정보
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# cctv 번호 및 위치(r, c) 리스트
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= maps[i][j] <= 5:
            cctvs.append((maps[i][j], i, j))
len_cctvs = len(cctvs)

# N, M <= 8이고 cctv의 갯수도 최대 8대이므로 브루트포싱의 가능성 존재...

# 순서대로 위 - 오른쪽 - 아래 - 왼쪽
default_moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
# cctv별 감시 범위
cctv_moves = defaultdict(list)

# 1번 cctv : 4가지
cctv_moves[1].append([0])
cctv_moves[1].append([1])
cctv_moves[1].append([2])
cctv_moves[1].append([3])
# 2번 cctv : 2가지
cctv_moves[2].append([0, 2])
cctv_moves[2].append([1, 3])
# 3번 cctv : 4가지
cctv_moves[3].append([0, 1])
cctv_moves[3].append([1, 2])
cctv_moves[3].append([2, 3])
cctv_moves[3].append([3, 0])
# 4번 cctv : 4가지
cctv_moves[4].append([0, 1, 2])
cctv_moves[4].append([1, 2, 3])
cctv_moves[4].append([2, 3, 0])
cctv_moves[4].append([3, 0, 1])
# 5번 cctv : 1가지
cctv_moves[5].append((0, 1, 2, 3))
# cctv의 방향을 정하는 갯수 : 4^8가지 = 2^16 = 1024 * 64 <= 10^5

def bruteforcing(idx, board):
    if idx >= len_cctvs:
        blinds = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0: blinds += 1
        global min_blinds
        if min_blinds > blinds:
            min_blinds = blinds
            # for row in board:
            #     print(row)
            # print()
        return
        
    current_cctv, _, _ = cctvs[idx]
    for views in cctv_moves[current_cctv]:
        new_board = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                new_board[i][j] = board[i][j]

        for move in views:
            _, r, c = cctvs[idx]
            dr, dc = default_moves[move]

            while 0 <= r + dr < N and 0 <= c + dc < M:
                if new_board[r + dr][c + dc] == 6:
                    break

                new_board[r + dr][c + dc] = 7
                r, c = r + dr, c + dc
        
        bruteforcing(idx + 1, new_board)

board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        board[i][j] = maps[i][j]
min_blinds = N * M
bruteforcing(0, board)

print(min_blinds)
