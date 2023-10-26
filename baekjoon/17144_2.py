# 백준 17144번: 미세먼지 안녕! (2회차)

import sys

input = sys.stdin.readline

# R, C <= 50, T <= 10^3
R, C, T = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for _ in range(R)]

top = (-1, -1)
bottom = (-1, -1)

for r in range(R):
    for c in range(C):
        if maps[r][c] == -1:
            top = (r - 1, c)
            bottom = (r, c)

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

t = 0

# 1초 동안 아래 적힌 일이 순서대로 일어난다.
while t < T:
    # 미세먼지가 확산된다.
    new_maps = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
            if maps[r][c] == 0: continue

            scatters = 0
            # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
            for dr, dc in moves:
                # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                if 0 <= r + dr < R and 0 <= c + dc < C:
                    if maps[r + dr][c + dc] != -1:
                        scatters += 1
                        # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                        new_maps[r + dr][c + dc] += int(maps[r][c] / 5)

            # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
            new_maps[r][c] += maps[r][c] - (int(maps[r][c] / 5) * scatters)

    maps = new_maps

    # 공기청정기가 작동한다.
    # 공기청정기에서는 바람이 나온다.
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
    
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고,
    for r in range(top[0] - 1, 0, -1):
        maps[r][0] = maps[r - 1][0]
    for c in range(C - 1):
        maps[0][c] = maps[0][c + 1]
    for r in range(top[0]):
        maps[r][C - 1] = maps[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        maps[top[0]][c] = maps[top[0]][c - 1]
    maps[top[0]][top[1] + 1] = 0

    # 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    for r in range(bottom[0] + 1, R - 1):
        maps[r][0] = maps[r + 1][0]
    for c in range(C - 1):
        maps[R - 1][c] = maps[R - 1][c + 1]
    for r in range(R - 1, bottom[0], -1):
        maps[r][C - 1] = maps[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        maps[bottom[0]][c] = maps[bottom[0]][c - 1]
    maps[bottom[0]][bottom[1] + 1] = 0

    t += 1

    # for row in maps:
    #     print(row)
    # print()

answer = 0
for row in maps:
    answer += sum(row)
print(answer + 2)
