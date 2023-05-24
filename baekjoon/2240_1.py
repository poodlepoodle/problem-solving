# 백준 2240번: 자두나무

import sys

input = sys.stdin.readline

# T <= 10^3, W <= 30
T, W = map(int, input().rstrip().split())

jadoos = [0]
for _ in range(T):
    jadoos.append(int(input()))

# dp[i][j][k]: i초에 j번 움직여서 먹을 수 있는 최대 자두의 개수
dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]

for i in range(1, T + 1):
    # 한 번도 움직이지 않았을 때: 자두가 1에서 떨어질 때만 먹은 자두 + 1
    dp[i][0] = dp[i - 1][0] + 1 if jadoos[i] == 1 else dp[i - 1][0]

    # 이동 횟수를 1번 ~ W번까지 움직이면서 체크
    for j in range(1, W + 1):
        if j > i: break

        # 자두가 1번 나무에서 떨어지고 그것을 받아 먹을 경우
        if jadoos[i] == 1 and j % 2 == 0:
            # 움직여서 받아먹을 것인가, 현재위치에서 받아먹을 것인가
            # 어짜피 이동한 횟수는 같다(지금 이동하거나 이전에 이동했거나)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # 자두가 2번 나무에서 떨어지고 그것을 받아 먹을 경우
        elif jadoos[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # 가만히 있든, 이동해서든, 자두를 받아 먹지 못하는 경우
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

for row in dp:
    print(row)
print()

print(max(dp[T]))
