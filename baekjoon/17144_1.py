import sys

input = sys.stdin.readline

R, C, T = map(int, input().rstrip().split())

# 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양
dusts = [list(map(int, input().rstrip().split())) for _ in range(R)]
Ar_top, Ar_bottom = -1, -1

for r in range(R):
    if dusts[r][0] == -1:
        Ar_top, Ar_bottom = r, r + 1
        break

moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
t = 0

# 1초 동안 아래 적힌 일이 순서대로 일어난다.
while t < T:
    # 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    diffusions = [[0 for _ in range(C)] for _ in range(R)]

    # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    for r in range(R):
        for c in range(C):
            if c == 0 and (r == Ar_top or r == Ar_bottom):
                continue

            cnt = 0
            for dr, dc in moves:
                # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                if 0 <= r + dr < R and 0 <= c + dc < C and dusts[r + dr][c + dc] != -1:
                    # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                    diffusions[r + dr][c + dc] += (dusts[r][c] // 5)
                    cnt += 1

            # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
            diffusions[r][c] += (dusts[r][c] - (dusts[r][c] // 5) * cnt)

    for r in range(R):
        for c in range(C):
            if c == 0 and Ar_top <= r <= Ar_bottom:
                continue
            dusts[r][c] = diffusions[r][c]

    # for row in dusts:
    #     print(row)
    # print()

    # 공기청정기가 작동한다. 공기청정기에서는 바람이 나온다.
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고,
    for r in range(Ar_top - 1, 0, -1):
        dusts[r][0] = dusts[r - 1][0]
        # print(r, 0)
    for c in range(0, C - 1):
        dusts[0][c] = dusts[0][c + 1]
        # print(0, c)
    for r in range(0, Ar_top):
        dusts[r][C - 1] = dusts[r + 1][C - 1]
        # print(r, C - 1)
    for c in range(C - 1, 1, -1):
        dusts[Ar_top][c] = dusts[Ar_top][c - 1]
        # print(Ar_top, c)
    dusts[Ar_top][1] = 0

    # 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    for r in range(Ar_bottom + 1, R - 1):
        dusts[r][0] = dusts[r + 1][0]
        # print(r, 0)
    for c in range(0, C - 1):
        dusts[R - 1][c] = dusts[R - 1][c + 1]
        # print(R - 1, c)
    for r in range(R - 1, Ar_bottom, -1):
        dusts[r][C - 1] = dusts[r - 1][C - 1]
        # print(r, C - 1)
    for c in range(C - 1, 1, -1):
        dusts[Ar_bottom][c] = dusts[Ar_bottom][c - 1]
        # print(Ar_bottom, c)
    dusts[Ar_bottom][1] = 0
    
    t += 1

answer = 2
for row in dusts:
    # print(row)
    answer += sum(row)
# print()

# 정답 출력    
print(answer)
