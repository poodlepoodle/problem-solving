# 백준 15486번: 퇴사 2

import sys

input = sys.stdin.readline

# N <= O(10^6)
N = int(input())

counsels = [(0, 0)]

for i in range(1, N + 1):
    T, P = map(int, input().rstrip().split())
    counsels.append((T, P))

# dp[i]: 1일 ~ i일까지 상담을 했을 때 얻을 수 있는 최대 이익
dp = [0] * (N + 51)

for i in range(1, N + 1):
    times, prices = counsels[i]
    dp[i] = max(dp[i - 1], dp[i])
    dp[i + times - 1] = max(dp[i + times - 1], dp[i - 1] + prices)

print(dp[N])
