# 백준 14889번: 스타트와 링크 (2회차)

from itertools import combinations
import sys

input = sys.stdin.readline

# N <= 20, 짝수
N = int(input())
stats = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 2개의 그룹으로 나누는 경우의 수는
# 브루트포싱: 20C10 = 20! / 10!(10!) = 20 * 19 * ... * 11 / 10 * 9 * ... * 1
# = 2 * 19 * 2 * 17 * 13 * 11 = 184756 < 10^6

# 각 그룹으로 나뉘었을 때 두 그룹의 능력 계산 -> O(N^2)
# 브루트포싱으로 시도는 해 볼만 함

answer = 40001
for group in combinations(range(N), N // 2):
    group = set(group)
    stat_A, stat_B = 0, 0

    for i in range(N):
        for j in range(N):
            if i == j: continue
            if i in group and j in group:
                stat_A += stats[i][j]
            elif i not in group and j not in group:
                stat_B += stats[i][j]
    answer = min(answer, abs(stat_A - stat_B))

print(answer)
