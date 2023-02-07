import sys

input = sys.stdin.readline

# 정사각행렬의 길이 N: 최대 4 * 10^2
N = int(input())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

main_diagonals = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        main_diagonals[i + 1][j + 1] = main_diagonals[i][j] + matrix[i][j]

# for row in main_diagonals:
#     print(row)
# print()

sub_diagonals = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N - 1, -1, -1):
        sub_diagonals[i + 1][j] = sub_diagonals[i][j + 1] + matrix[i][j]

# for row in sub_diagonals:
#     print(row)
# print()

max_beauty = 0

for size in range(2, N + 1): # 2, 3, ..., N -> O(N)
    for r in range(N - size + 1): # 0, 1, ..., N - size -> O(N)
        for c in range(N - size + 1): # 0, 1, ..., N - size -> O(N)
            beauty = (main_diagonals[r + size][c + size] - main_diagonals[r][c])
            beauty -= (sub_diagonals[r + size][c] - sub_diagonals[r][c + size])

            # print(beauty)
            max_beauty = max(max_beauty, beauty)

print(max_beauty)
