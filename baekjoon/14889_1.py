# 14889번: 스타트와 링크

from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input()) # N <= 20
ability = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 모든 조합의 경우의 수의 최댓값(N = 20): 20C10 < 2 * 10^6

answer = 20001

for team_A in combinations(range(N), N // 2):
    team_B = [i for i in range(N) if i not in team_A]
    
    team_ability_A = 0
    for i, j in combinations(team_A, 2):
        team_ability_A += (ability[i][j] + ability[j][i])
    team_ability_B = 0
    for i, j in combinations(team_B, 2):
        team_ability_B += (ability[i][j] + ability[j][i])

    answer = min(answer, abs(team_ability_A - team_ability_B))

print(answer)
