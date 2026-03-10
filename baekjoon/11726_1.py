# 백준 11726번: 2xn 타일링

import sys

input = sys.stdin.readline

# N <= 10^3
N = int(input())
if N == 1:
    print(1)
    sys.exit()

# 포인트: 위아래 막대기가 가로로 어긋나게 놓이는 경우는 그 순간부터 네모가 될 수 없음


# dp[i] = 2*i를 채우는 방법의 수
dp = [0 for _ in range(N + 1)]
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[N])
