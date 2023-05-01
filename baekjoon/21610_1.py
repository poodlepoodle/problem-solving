# 백준 21610번: 마법사 상어와 비바라기

from collections import deque
import sys

input = sys.stdin.readline

# N, M <= 10^2
N, M = map(int, input().rstrip().split())

# 각 격자의 바구니의 물의 양 A[r][c]
A = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 구름은 칸 전체를 차지한다.
clouds = deque([[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]])

# 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다.
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다.
moves = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

# 이동을 명령하면 다음이 순서대로 진행된다.
for _ in range(M): # 10^2
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    D, S = map(int, input().rstrip().split())
    Sr, Sc = moves[D - 1][0] * S, moves[D - 1][1] * S

    # 10^4
    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + Sr + N) % N
        clouds[i][1] = (clouds[i][1] + Sc + N) % N

    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for r, c in clouds:
        A[r][c] += 1

    # 3. 구름이 모두 사라진다.
    is_cloud_now = [[False for _ in range(N)] for _ in range(N)]
    # current_clouds = next_clouds[:]
    # next_clouds.clear()

    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    for r, c in clouds:
        cnt = 0
        is_cloud_now[r][c] = True

        # 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
        for idx in range(1, 8, 2):
            dr, dc = moves[idx]
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if A[r + dr][c + dc]: cnt += 1
        
        # (r, c)에 있는 바구니의 물이 양이 증가한다.
        A[r][c] += cnt

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    len_prevs = len(clouds)
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and not is_cloud_now[r][c]:
                clouds.append([r, c])
                A[r][c] -= 2

    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for _ in range(len_prevs):
        clouds.popleft()

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
answer = 0
for row in A:
    answer += sum(row)
print(answer)
