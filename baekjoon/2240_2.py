# 백준 2240번: 자두나무 (2회차)

import sys

input = sys.stdin.readline

# T <= 10^3
# W <= 30
T, W = map(int, input().rstrip().split())

# 관찰
#   누가 봐도 DP 문제
#   최초에는 1번에 위치
#   매 초마다 이동하는 경우와 이동하지 않는 경우의 자두 먹은 개수를 세야 할 듯
# DP 점화식
#   dp[i][j][k] = i초에 j번 나무 밑에 k번 이동해서 도착했을 때 먹을 수 있는 최대 자두 개수?
# 1차 접근 후 피드백
#   j는 k가 홀수, 짝수인지에 따라서 자동으로 결정되는 변수임, 나무가 2개뿐이기 때문
# 개선된 DP 점화식
#   dp[i][j] = i초에 j번 이동해서 도착했을 때 먹을 수 있는 최대 자두 개수

dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]
dp[0][0] = 0

def print_dp(plum_drop):
    print('      O' if plum_drop == 1 else '         O')
    for idx, row in enumerate(dp[1:]):
        print(f'  {idx + 1}초', row)

for i in range(1, T + 1):
    plum_drop = int(input())
    # print(f'{i}초, {plum_drop}번 나무에서 떨어짐')

    for j in range(min(i + 1, W + 1)):
        current_tree = j % 2 + 1

        if j == 0:
            if current_tree == plum_drop:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j]
            continue

        if current_tree == plum_drop:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

    # print_dp(plum_drop)
    # print()

print(max(dp[T]))
