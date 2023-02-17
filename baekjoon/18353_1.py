import sys

input = sys.stdin.readline

# N <= 2 * 10^3
N = int(input())
arr = list(map(int, input().rstrip().split()))
arr.insert(0, 0)

# 전투력 총합이 최대가 되는 것이 아니라, 남아 있는 병사의 수가 최대로 되는 것을 원함
# dp[i] = max(dp[1 <= j <= i - 1]) + 1
# 즉, dp[i]는 dp[0]부터 dp[i - 1]까지의 값들 중 i < j인 값들에 한해 가장 큰 값에 1을 더한 값임
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    max_value = 0
    for j in range(1, i):
        if arr[i] < arr[j]:
            max_value = max(max_value, dp[j])

    dp[i] = max_value + 1

print(N - max(dp))
