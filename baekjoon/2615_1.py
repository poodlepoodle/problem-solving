import sys

input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for _ in range(19)]

# 19 * 19 = 361 ^ 10^3
# 8방향까지 6개 검사 = 48 < 10^2
# 결과는 10^5 내에 통과될 것으로 기대

# 우상 - 우 - 우하 - 하 - 좌하 - 좌 - 좌상 - 상 순서지만, 실제로 거의 첫 4개만 많이 씀
moves = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
win = 0
answer = [-1, -1]

for r in range(19):
    for c in range(19):
        mark = board[r][c]

        if not mark: continue
        # print(r, c)

        for idx in range(4):
            dr, dc = moves[idx]

            cnt = 1
            cur_r, cur_c = r, c
            
            while (0 <= cur_r + dr < 19) and (0 <= cur_c + dc < 19) and board[cur_r + dr][cur_c + dc] == mark:
                cur_r += dr
                cur_c += dc
                cnt += 1

            # 육목 검사
            if cnt == 5:
                dr, dc = moves[(idx + 4) % 8]

                if not ((0 <= r + dr < 19) and (0 <= c + dc < 19) and board[r + dr][c + dc] == mark):
                    win = mark
                    answer = (r, c)

        # print()

        if win: break
    if win: break

print(win)
if win:
    print(answer[0] + 1, answer[1] + 1)
