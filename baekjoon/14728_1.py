# 백준 14728번: 벼락치기

import sys
input = sys.stdin.readline

# N <= 10^2
# T <= 10^4
N, T = map(int, input().rstrip().split())

# costs[i], profits[i]: i번째 단원을 공부했을 때의 비용과 이득
costs = [0]
profits = [0]
for _ in range(N):
    cost, profit = map(int, input().rstrip().split())
    costs.append(cost)
    profits.append(profit)

# dp[i][j]: j초 동안 1 ~ i단원까지 중 얻을 수 있는 최고 점수
dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
answer = 0

for i in range(1, N + 1):
    for j in range(T + 1):
        cost, profit = costs[i], profits[i]
        if cost <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + profit)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][T])
