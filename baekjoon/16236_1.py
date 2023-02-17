import sys
from collections import deque

input = sys.stdin.readline

# 최대 20
N = int(input())

spaces = [list(map(int, input().rstrip().split())) for _ in range(N)]
shark_r, shark_c = N, N
# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치
for i in range(N):
    for j in range(N):
        if spaces[i][j] == 9:
            shark_r, shark_c = i, j
            spaces[i][j] = 0

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
shark_size = 2
shark_cnt = 0

# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기
# 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

answer = 0

while True:
    # 먹을 수 있는 물고기 리스트 뽑기
    target_fishes = []
    for i in range(N):
        for j in range(N):
            if 1 <= spaces[i][j] < shark_size:
                target_fishes.append((i, j))

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 종료
    if len(target_fishes) == 0:
        break

    # BFS 초기화
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    q.append((shark_r, shark_c, 0))
    visited[shark_r][shark_c] = True

    # 이번 물고기를 먹기 위해 이동한 횟수
    moved_time = 1e9
    moved_r, moved_c = N, N

    while q:
        r, c, level = q.popleft()

        # BFS를 중단해도 되는 경우
        if moved_time < level:
            break

        # 어떤 물고기를 먹을 수 있게 되는 경우
        if (r, c) in target_fishes:
            # 아래 조건들에 만족하면서 우선순위가 더 높으면 최종적으로 먹을 물고기를 변경
            if moved_time > level:
                moved_time = level
                moved_r, moved_c = r, c
                # print(f'case 1, -> {r}, {c}')
            elif moved_time == level and moved_r > r:
                moved_r, moved_c = r, c
                # print(f'case 2, -> {r}, {c}')
            elif moved_time == level and moved_r == r and moved_c > c:
                moved_c = c
                # print(f'case 3, -> {r}, {c}')

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if not visited[r + dr][c + dc] and spaces[r + dr][c + dc] <= shark_size:
                    q.append((r + dr, c + dc, level + 1))
                    visited[r + dr][c + dc] = True

    if moved_time == 1e9:
        break

    # 상어가 물고기 먹었을 때 처리
    shark_r, shark_c = moved_r, moved_c
    spaces[shark_r][shark_c] = 0
    shark_cnt += 1
    answer += moved_time

    if shark_cnt == shark_size:
        shark_size, shark_cnt = shark_size + 1, 0

    # for row in spaces:
    #     print(row)
    # print()

print(answer)
