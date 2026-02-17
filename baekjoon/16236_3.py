# 백준 16236번: 아기 상어 (3회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 20
N = int(input())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 포인트
#   1. 아기 상어는 자신과 작거나 같은 경우 지나칠 수 있음
#   2. 아기 상어는 자신과 작은 경우 먹을 수 있음
#   3. 아기 상어는 먹을 수 있는 먹이 중에서는 가장 가까운 먹이를 먹음
#   4. 가장 가까운 먹이가 여러 개라면, Z 순서로 먹이를 먹음
#   5. 먹을 수만 있다면, 크기가 더 작느냐는 중요치 않고 거리가 중요하다는 점 명심
#   6. 이 때의 거리는 유클리디안 거리가 아닌, BFS 이동 거리라는 점 명심
# 아이디어
#   1. 현재 아기 상어로부터 BFS 수행, 먹을 수 있는 먹이 후보를 모두 선정 -> O(N^2)
#   2. 먹을 수 있는 먹이 후보 중 가장 좌상에 있는 먹이를 먹음 -> O(N^2)
#   3. 이 과정을 모든 먹이 개수만큼 반복 -> O(N^2)

moves = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]

shark_r, shark_c = -1, -1
shark_size = 2
shark_eaten = 0
for r in range(N):
    for c in range(N):
        if maps[r][c] == 9:
            maps[r][c] = 0
            shark_r, shark_c = r, c

def is_in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def is_can_pass(r, c):
    global shark_size
    return maps[r][c] <= shark_size

def is_can_eat(r, c):
    global shark_size
    return 1 <= maps[r][c] < shark_size

def find_all_catchable_fishes(r, c):
    global shark_size
    q = deque()
    visited = [[404 for _ in range(N)] for _ in range(N)]
    candidates = []

    q.append((r, c, 0))
    visited[r][c] = 0

    while q:
        r, c, moved = q.popleft()

        for dr, dc in moves:
            if is_in_board(r + dr, c + dc) and is_can_pass(r + dr, c + dc) and visited[r + dr][c + dc] > moved + 1:
                if is_can_eat(r + dr, c + dc):
                    candidates.append((r + dr, c + dc, moved + 1))
                    visited[r + dr][c + dc] = moved + 1
                else:
                    q.append((r + dr, c + dc, moved + 1))
                    visited[r + dr][c + dc] = moved + 1

    return candidates

def find_one_fish_to_eat(candidates):
    candidates.sort(key=lambda x:(x[2], x[0], x[1]))
    return candidates[0]

answer = 0
while True:
    candidates = find_all_catchable_fishes(shark_r, shark_c)
    # print(candidates)
    if len(candidates) == 0: break

    fr, fc, fmoved = find_one_fish_to_eat(candidates)
    # print(fr, fc, fmoved)
    maps[fr][fc] = 0
    shark_r, shark_c = fr, fc
    answer += fmoved
    # print('---------------')
    # for row in maps:
    #     print(row)
    # print('shark in', (shark_r, shark_c))

    shark_eaten += 1
    if shark_eaten >= shark_size:
        shark_size += 1
        shark_eaten = 0
    # print('shark size is', shark_size)

    # print('---------------')
    # print('answer:', answer)
    # print()

print(answer)
