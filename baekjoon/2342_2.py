# 백준 2342번: Dance Dance Revolution

import sys

input = sys.stdin.readline

commands = list(map(int, input().rstrip().split()))
N = len(commands) - 1

# dp[i][j][k] = i번째 발판을 밟은 시점에 왼발이 j, 오른발이 k에 있을 때 최소 누적 리소스
# dp = [[[int(1e9) for _ in range(5)] for _ in range(5)] for _ in range(len(commands) + 1)]
dp = [[[int(1e9) for _ in range(5)] for _ in range(5)] for _ in range(len(commands) + 1)]

powers = {
    0: {
        1: 2,
        2: 2,
        3: 2,
        4: 2
    },
    1: {
        1: 1,
        2: 3,
        3: 4,
        4: 3
    },
    2: {
        1: 3,
        2: 1,
        3: 3,
        4: 4
    },
    3: {
        1: 4,
        2: 3,
        3: 1,
        4: 3
    },
    4: {
        1: 3,
        2: 4,
        3: 3,
        4: 1
    }
}

dp[0][0][0] = 0

first_step = commands[0]
dp[1][0][first_step] = 2
dp[1][first_step][0] = 2

# for row in dp[:2]:
#     for col in row:
#         print(col)
#     print()
# print()

for i in range(1, len(commands) - 1):
    new_step = commands[i]
    # print('new_step:', new_step)

    for j in range(5): # 왼발
        for k in range(5): # 오른발
            if dp[i][j][k] >= int(1e9): continue

            if j != new_step:
                dp[i + 1][j][new_step] = min(dp[i + 1][j][new_step], dp[i][j][k] + powers[k][new_step])
            if new_step != k:
                dp[i + 1][new_step][k] = min(dp[i + 1][new_step][k], dp[i][j][k] + powers[j][new_step])
    
    # for row in dp[i + 1:i + 2]:
    #     for col in row:
    #         print(col)
    #     print()
    # print()

print(min([min(row) for row in dp[N]]))
