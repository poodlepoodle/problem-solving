# 백준 21610번: 마법사 상어와 비바라기 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 50
# M <= 10^2
N, M = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
queries = [list(map(int, input().rstrip().split())) for _ in range(M)]

# 시간복잡도 계산
#   1. 모든 구름이 이동 -> O(N^2) ~= 10^3
#   2. 각 구름에서 비가 내려 물이 증가 -> O(N^2) ~= 10^3
#   3. 물복사버그 마법 시전 -> O(N^2) ~= 10^3
#   3. 위 모든 과정을 10^2번 반복

moves = {
    1: [0, -1],
    2: [-1, -1],
    3: [-1, 0],
    4: [-1, 1],
    5: [0, 1],
    6: [1, 1],
    7: [1, 0],
    8: [1, -1],
}

clouds = deque()
clouds.append((N - 2, 0))
clouds.append((N - 2, 1))
clouds.append((N - 1, 0))
clouds.append((N - 1, 1))

def is_in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def print_board():
    print('-----------')
    for row in maps:
        print(row)

def clouds_move(di, si):
    prev_clouds = []
    increased_buckets = []

    # 모든 구름이 di 방향으로 si만큼 이동
    while clouds:
        r, c = clouds.popleft()
        dr, dc = moves[di]
        new_r, new_c = (r + dr * si + N * 2) % N, (c + dc * si + N * 2) % N
        # 각 구름에서 비가 내려 바구니의 물 1 증가
        maps[new_r][new_c] += 1
        increased_buckets.append((new_r, new_c))
        # 구름이 모두 사라짐
        prev_clouds.append((new_r, new_c))

    return prev_clouds, increased_buckets

def water_duplication(buckets):
    # 대각선 방향으로 거리가 1인 물이 있는 바구니 수만큼 물 증가
    for r, c in buckets:
        cnt = 0
        for direction in [2, 4, 6, 8]:
            dr, dc = moves[direction]
            if is_in_board(r + dr, c + dc) and maps[r + dr][c + dc]:
                cnt += 1
        maps[r][c] += cnt

def generate_new_clouds(prev_clouds):
    prev_clouds = set(prev_clouds)
    for r in range(N):
        for c in range(N):
            # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생김
            if maps[r][c] >= 2 and (r, c) not in prev_clouds:
                clouds.append((r, c))
                # 해당하는 칸의 물이 2씩 줄어듦
                maps[r][c] -= 2

# print_board()
for di, si in queries:
    # print((di, si))
    prev_clouds, buckets = clouds_move(di, si)
    # print_board()
    water_duplication(buckets)
    # print_board()
    generate_new_clouds(prev_clouds)
    # print_board()
    # print()

print(sum([sum(row) for row in maps]))
