# 백준 14501번: 퇴사 (2회차)

import sys

input = sys.stdin.readline

# 총 일수 N <= 15
N = int(input())

# dp[i] = i번째 날까지 상담했을 때 얻을 수 있는 최대 이익
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    Ti, Pi = map(int, input().rstrip().split())
    # print(f'{i}일 ~ {i + Ti - 1}일까지, 보상 {Pi}')
    
    # print(i + Ti - 1, N)
    if i + Ti - 1 <= N:
        # print(dp[i + Ti - 1], dp[i - 1] + Pi)
        dp[i + Ti - 1] = max(dp[i + Ti - 1], dp[i - 1] + Pi)
    dp[i] = max(dp[i - 1], dp[i])
    # print(dp[1:])
    # print()

print(dp[-1])
