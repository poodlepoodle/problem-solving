from itertools import combinations
import sys

def input(): return sys.stdin.readline().rstrip()

# N의 최댓값 50, M의 최댓값 13
N, M = map(int, input().split())

# 0은 빈 칸, 1은 집, 2는 치킨집
# 집의 최대 갯수 100, 치킨집의 최대 갯수 13
maps = [list(map(int, input().split())) for _ in range(N)]

houses = []
total_chicks = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append((i, j))
        elif maps[i][j] == 2:
            total_chicks.append((i, j))

# 치킨집 최대 13개 중 M개를 고르는 경우의 최대 갯수
# -> 13CM = 13 * 12 * ... * 7 / 6 * 5 * 4 * 3 * 2 * 1 -> 매우 크지는 않은 수... (약 1700)

# 각 치킨집의 조합이 골라졌을 때 모든 치킨 거리를 구하는 갯수 : 100 * 13 -> 1300

# 이상하게 경우의 수가 크지 않다?? -> 완전 탐색 시도

# 치킨집 M개 정하는 조합 구하기
answer = 1e9
for chicks in combinations(total_chicks, M):
    chick_sum = 0
    for house in houses:
        min_house_chick = 2 * N
        for chick in chicks:
            temp = abs(house[0] - chick[0]) + abs(house[1] - chick[1])
            min_house_chick = min(min_house_chick, temp)
        
        chick_sum += min_house_chick

    answer = min(answer, chick_sum)

print(answer)
