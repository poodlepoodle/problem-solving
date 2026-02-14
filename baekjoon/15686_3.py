# 백준 15686번: 치킨 배달 (3회차)

import sys

from itertools import combinations
input = sys.stdin.readline

# N <= 50
# M <= 13
N, M = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 브루트포싱 계산
# 도시에 있는 모든 치킨집 중 M개 조합: 
#   치킨집 개수 <= 13개
#   13개 중 M개를 고르는 경우의 수 <= 13M6 = 1716 ~= 10^3
# 도시에 있는 모든 집 순회 = 2M <= 26 ~= 10^2
# 각 집마다 모든 치킨집 돌면서 치킨 거리 계산 = M = 13 ~= 10
# 결론
#   브루트포싱 시도해볼 만 함

HOUSE = 1
CHICKEN = 2
all_houses = []
all_chickens = []

for r in range(N):
    for c in range(N):
        if maps[r][c] == HOUSE:
            all_houses.append((r, c))
            maps[r][c] = 0
        elif maps[r][c] == CHICKEN:
            all_chickens.append((r, c))
            maps[r][c] = 0

def distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

answer = int(1e9)
for chickens in combinations(all_chickens, M):
    current_answer = 0
    for house in all_houses:
        dist = 99
        for chicken in chickens:
            dist = min(dist, distance(house, chicken))
        current_answer += dist
    answer = min(answer, current_answer)

print(answer)
