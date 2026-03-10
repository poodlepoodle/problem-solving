# 백준 12852번: 1로 만들기 2

import sys

input = sys.stdin.readline

# N <= 10^6
N = int(input())

# dp[i]: i를 1로 만들기 위한 최소 횟수
dp = [i - 1 for i in range(N + 1)]
# parents[i] = i를 1로 만들기 위해 직전에 거친 수
parents = [i - 1 for i in range(N + 1)]

for i in range(1, N + 1):
    # print(i)
    if dp[i] > dp[i - 1] + 1:
        dp[i] = dp[i - 1] + 1
        parents[i] = i - 1
    if i * 3 <= N and dp[i * 3] > dp[i] + 1:
        dp[i * 3] = dp[i] + 1
        parents[i * 3] = i
    if i * 2 <= N and dp[i * 2] > dp[i] + 1:
        dp[i * 2] = dp[i] + 1
        parents[i * 2] = i
#     print(*range(1, N + 1))
#     print('----------')
#     print(*dp[1:])
#     print(*parents[1:])
#     print()

print(dp[N])

answer = [N]
current = N
while current > 1:
    current = parents[current]
    answer.append(current)
print(*answer)
