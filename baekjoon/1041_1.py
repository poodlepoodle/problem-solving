# 백준 1041번: 주사위

import sys
input = sys.stdin.readline

# N <= 10^6
N = int(input())
# each number <= 50
dices = list(map(int, input().rstrip().split()))
A, B, C, D, E, F = dices

parallels = [
    min(A, F),
    min(C, D),
    min(B, E)
]
parallels.sort()

if N == 1:
    print(sum(dices) - max(dices))
    sys.exit()

# min_1 = min(dices)
# min_2 = min([
#     A + B,
#     A + C,
#     A + D,
#     A + E,
#     B + C,
#     B + D,
#     B + F,
#     C + E,
#     C + F,
#     D + E,
#     D + F,
#     E + F
# ])
# min_3 = min([
#     A + B + C,
#     A + B + D,
#     A + C + E,
#     A + D + E,
#     B + C + F,
#     B + D + F,
#     C + E + F,
#     D + E + F
# ])
# print(min_1)
# print(min_2)
# print(min_3)

min_1 = parallels[0]
min_2 = parallels[0] + parallels[1]
min_3 = sum(parallels)

# 접근
#   N == 2일 때는?
#       1. (맨 위층, 꼭지점의) 주사위 4개는 인접한 3개 면씩만 공개
#       2. (맨 아래층, 꼭지점의) 주사위 4개는 인접한 2개 면씩만 공개
#   N == 3일 때는?
#       1. (3층, 꼭지점의) 주사위 4개는 인접한 3개 면씩만 공개
#       2. (3층, 꼭지점을 제외한 가장자리) 주사위 1 * 4 = 4개는 인접한 2개 면씩만 공개
#       3. (3층, 나머지) 주사위 3 * 3 - (4 + 4) = 1개는 인접한 1개 면만 공개
#       4. (1 ~ 2층, 꼭지점) 주사위 3 - 1 = 2층 * 4면 = 8개는 인접한 2개 면씩만 공개
#       5. (1 ~ 2층, 꼭지점을 제외한 가장자리) 주사위 2층 * 4면 = 8개는 인접한 1개 면만 공개
#   N == N일 때는?
#       1. (N층, 꼭지점의) 주사위 4개는 인접한 3개 면씩만 공개
#       2. (N층, 꼭지점을 제외한 가장자리) 주사위 4N - 8개는 인접한 2개 면씩만 공개
#       3. (N층, 나머지) 주사위 N^2 - 4N + 4개는 인접한 1개 면만 공개
#       4. (1 ~ N-1층, 꼭지점) 주사위 4N - 4개는 인접한 2개 면씩만 공개
#       5. (1 ~ N-1층, 꼭지점을 제외한 가장자리) 주사위 N^2 - 3N + 2개는 인접한 1개 면만 공개

answer = 0
answer += min_3 * 4
answer += min_2 * (4 * N - 8)
answer += min_1 * (N - 2)**2
answer += min_2 * 4 * (N - 1)
answer += min_1 * 4 * (N - 2) * (N - 1)
print(answer)
