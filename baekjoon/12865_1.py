# 백준 12865번: 평범한 배낭 풀이

import sys

input = sys.stdin.readline

# N <= 10^2, K <= 10^5
N, K = map(int, input().rstrip().split())

weight = [0]
value = [0]

for _ in range(1, N + 1):
    # W: 무게, V: 가치
    W, V = map(int, input().rstrip().split())

    weight.append(W)
    value.append(V)

# dp[i][w]: 1번째 ~ i번째 물건까지 고려하고 배낭의 용량이 최대 w일 때 얻을 수 있는 최대 가치
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 아무 물건도 담지 않으려고 하는 경우
for w in range(K + 1):
    dp[0][w] = 0

# 배낭의 용량이 0인 경우
for i in range(N + 1):
    dp[i][0] = 0

# for row in dp:
#     print(row)
# print()

for i in range(1, N + 1):
    for w in range(1, K + 1):
        # 현재 고려하는 물건의 무게(weight[idx])가 설정한 배낭 용량(w)보다 작거나 같다면 담기
        if weight[i] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i]] + value[i])
        else:
            dp[i][w] = dp[i - 1][w]
            
        # for row in dp:
        #     print(row)
        # print()

# for row in dp:
#     print(row)
# print()

print(dp[N][K])
