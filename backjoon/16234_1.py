from collections import deque
import sys

input = sys.stdin.readline

# N <= 50
N, L, R = map(int, input().rstrip().split())

countries = [list(map(int, input().rstrip().split())) for _ in range(N)]

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

def move(i, j, visited):
    q = deque([(i, j)])
    moved_countries = []
    moved_population = 0

    while q:
        r, c = q.popleft()

        moved_population += countries[r][c]
        moved_countries.append((r, c))

        for dr, dc in directions:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if not visited[r + dr][c + dc] and L <= abs(countries[r][c] - countries[r + dr][c + dc]) <= R:
                    q.append((r + dr, c + dc))
                    visited[r + dr][c + dc] = True

    if len(moved_countries) == 1: return False
    else: return moved_countries

day = 0
while True:
    # 전체 국가들에 대해서 국경선을 열어야 하는 경우가 있는지 검사
    visited = [[False for _ in range(N)] for _ in range(N)]
    moved_countries = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                # print(f"move({i}, {j})")
                moved_set = move(i, j, visited)
                if moved_set:
                    moved_countries.append(moved_set)
                # print(len(moved_sets))
                # for row in countries:
                #     print(row)
                # print()

    # 인구 이동이 일어나지 않는다면 종료
    if not len(moved_countries):
        break

    day += 1

    for moved_set in moved_countries:
        population = sum([countries[i][j] for i, j in moved_set]) // len(moved_set)
        for i, j in moved_set:
            countries[i][j] = population

print(day)
