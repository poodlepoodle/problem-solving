import sys

input = sys.stdin.readline

# 최대 10^6
N = int(input())

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

dp = [1e9] * (3 * (N + 1))
dp[1] = 0

# 1 -> 0번
# 1 + 1 -> 1번
# 1 * 2 -> 1번
# 1 * 3 -> 1번

for i in range(1, N + 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    dp[i * 3] = min(dp[i * 3], dp[i] + 1)

print(dp[N])
