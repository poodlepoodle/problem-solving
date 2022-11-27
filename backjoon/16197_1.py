import sys
sys.setrecursionlimit(10**5)

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

# 둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.

# o: 동전
# .: 빈 칸
# #: 벽

# 4^10의 선택지 -> 충분히 탐색해볼만함...

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bruteforcing(coin_1, coin_2, depth):
    global answer
    r1, c1 = coin_1
    r2, c2 = coin_2

    # 다음번에 이동하면 10번보다 많이 이동하는 경우 -> 거름
    if depth >= answer: return
    if depth >= 10: return
    # 동전이 겹친 경우 -> 거름
    if r1 == r2 and c1 == c2: return

    # 두 동전이 이동할 수 있는 상하좌우 4방향에 대해
    for dr, dc in directions:
        next_r1, next_c1 = r1 + dr, c1 + dc
        next_r2, next_c2 = r2 + dr, c2 + dc

        # 두개 다 떨어지는 경우 -> 거름
        if (next_r1 < 0 or next_r1 >= N or next_c1 < 0 or next_c1 >= M) \
            and (next_r2 < 0 or next_r2 >= N or next_c2 < 0 or next_c2 >= M):
            continue
        # 두개 다 안 떨어지는 경우 -> 이동
        elif (0 <= next_r1 < N and 0 <= next_c1 < M) \
            and (0 <= next_r2 < N and 0 <= next_c2 < M):
            if board[next_r1][next_c1] != '#':
                next_coin_1 = (next_r1, next_c1)
            else:
                next_coin_1 = (r1, c1)
            if board[next_r2][next_c2] != '#':
                next_coin_2 = (next_r2, next_c2)
            else:
                next_coin_2 = (r2, c2)
            
            bruteforcing(next_coin_1, next_coin_2, depth + 1)
        # 두개 중 하나만 나가는 경우
        else:
            # print(coin_1, coin_2, depth)
            answer = min(answer, depth + 1)
            return
    return

answer = int(1e9)
bruteforcing(coins[0], coins[1], 0)

print(answer if answer != int(1e9) else -1)
