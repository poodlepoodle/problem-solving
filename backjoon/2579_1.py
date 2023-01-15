import sys

input = sys.stdin.readline

N = int(input())

# 계단 별 점수
P = [0]
for _ in range(N):
    P.append(int(input()))

# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

# dp[i] : i번째 계단까지 도달했을 때 얻을 수 있는 최대 점수
dp = [0] * (N + 1)

# 점화식 : dp[i] = max(dp[i - 2], dp[i - 3] + P[i - 1]) + P[i]

if N == 1:
    print(P[1])
    exit()
elif N == 2:
    print(P[1] + P[2])
    exit()
elif N == 3:
    print(max(P[1] + P[3], P[2] + P[3]))
    exit()

dp[1] = P[1]
dp[2] = P[1] + P[2]
dp[3] = max(P[1] + P[3], P[2] + P[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + P[i - 1]) + P[i]

print(dp[N])
