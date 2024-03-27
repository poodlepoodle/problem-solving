# 15686번: 치킨 배달 (2회차)

from itertools import combinations
import sys

input = sys.stdin.readline

# N <= 50, M <= 13
N, M = map(int, input().rstrip().split())

houses = []
chickens = []

# 0은 빈 칸, 1은 집, 2는 치킨집
for r in range(N):
    line = list(map(int, input().rstrip().split()))

    for c in range(N):
        if line[c] == 2: chickens.append((r, c))
        elif line[c] == 1: houses.append((r, c))

# print(houses)
# print(chickens)

answer = int(1e9)

for current_chickens in combinations(chickens, M):
    current_total_cost = 0

    for hr, hc in houses:
        current_house_cost = int(1e9)
        for cr, cc in current_chickens:
            current_house_cost = min(current_house_cost, abs(hr - cr) + abs(hc - cc))

        if answer <= current_total_cost: break
        current_total_cost += current_house_cost

    if answer <= current_total_cost: continue
    answer = min(answer, current_total_cost)

print(answer)
