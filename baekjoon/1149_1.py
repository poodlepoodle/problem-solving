# 백준 1149번: RGB거리

import sys

input = sys.stdin.readline

# N <= 10^3
N = int(input())
costs = [list(map(int, input().rstrip().split())) for _ in range(N)]

# dp[i][j]: i번째 집을 j색으로 칠했을 때까지 최소 비용
dp = [[int(1e9) for _ in range(3)] for _ in range(N + 1)]
for j in range(3):
    dp[0][j] = 0

for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1][2]

    # for row in dp:
    #     print(row)
    # print()
print(min(dp[N]))
