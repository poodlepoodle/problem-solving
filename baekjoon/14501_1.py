import sys

input = sys.stdin.readline

# 최대 15
N = int(input())

counsels = [list(map(int, input().rstrip().split())) for _ in range(N)]

# i번째 날까지 얻을 수 있는 최대 이익
dp = [0] * (N + 1)

for i, (t, p) in enumerate(counsels):
    print(i, t, p)

    if i + t <= N:
        dp[i + t] = max(dp[i + t], p)

print(dp)

