# 백준 2579번: 계단 오르기 (2회차)

import sys

input = sys.stdin.readline

# N <= 10^4
N = int(input())
scores = [0]
scores.extend([int(input()) for _ in range(N)])
# print('scores:', scores[1:])

if N == 1:
    print(scores[1])
    sys.exit()

# dp[i][j]: i번째 계단에 연속으로 j개의 계단을 밟은 상태로 도착 시 얻을 수 있는 최고 점수
dp = [[0 for _ in range(3)] for _ in range(N + 1)]
dp[1][1] = scores[1]
dp[1][2] = scores[1]
dp[2][1] = scores[2]
dp[2][2] = scores[1] + scores[2]

for i in range(3, N + 1):
    # 1. 전전 계단에서 뛰어 올라오는 경우
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + scores[i]
    # 2. 전 계단에서 걸어 올라오는 경우
    dp[i][2] = dp[i - 1][1] + scores[i]
    # for row in dp[1:]:
    #     print(row[1:])
    # print()

print(max(dp[N]))
