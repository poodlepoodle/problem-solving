# 20056번: 마법사 상어와 파이어볼

from collections import deque
import sys

input = sys.stdin.readline

# N <= 50, M <= 3 * 10^3, K <= 10^3
N, M, K = map(int, input().rstrip().split())

maps = [[0 for _ in range(N)] for _ in range(N)]
f_masses = [[0 for _ in range(N)] for _ in range(N)]
f_directions = [[[] for _ in range(N)] for _ in range(N)]
f_speeds = [[0 for _ in range(N)] for _ in range(N)]

fireballs = deque()

for _ in range(M):
    r, c, mass, speed, direction = map(int, input().rstrip().split())
    fireballs.append((r - 1, c - 1, mass, speed, direction))

# print(fireballs)

moves = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

for _ in range(K):
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    while fireballs:
        r, c, mass, speed, direction = fireballs.popleft()

        # 질량이 0인 파이어볼은 소멸되어 없어진다.
        if mass == 0: continue

        dr, dc = moves[direction]
        r, c = (r + speed * dr + N * 1000) % N, (c + speed * dc + N * 1000) % N
        maps[r][c] += 1
        f_masses[r][c] += mass
        f_directions[r][c].append(direction)
        f_speeds[r][c] += speed

    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    for r in range(N):
        for c in range(N):
            if maps[r][c] >= 1:
                if maps[r][c] == 1:
                    fireballs.append((r, c, f_masses[r][c], f_speeds[r][c], f_directions[r][c][0]))
                else:
                    new_mass = f_masses[r][c] // 5
                    new_speed = f_speeds[r][c] // maps[r][c]
                    if len(set([d % 2 for d in f_directions[r][c]])) == 1:
                        new_directions = [0, 2, 4, 6]
                    else:
                        new_directions = [1, 3, 5, 7]

                    for d in new_directions:
                        fireballs.append((r, c, new_mass, new_speed, d))

                maps[r][c] = 0
                f_masses[r][c] = 0
                f_directions[r][c].clear()
                f_speeds[r][c] = 0

answer = 0

# print(fireballs)

while fireballs:
    _, _, mass, _, _ = fireballs.popleft()
    answer += mass

print(answer)
