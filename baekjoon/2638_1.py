# 백준 2638번: 치즈

from collections import deque
import sys

input = sys.stdin.readline

# N, M <= 10^2
N, M = map(int, input().rstrip().split())

cheeze = [list(map(int, input().rstrip().split())) for _ in range(N)]

# for row in cheeze:
#     print(row)
# print()

# 0부터 상, 우, 하, 좌
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(air):
    q = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for r, c in air:
        visited[r][c] = 1
        q.append((r, c))

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < M:
                # 치즈에 닿았을 경우
                if cheeze[r + dr][c + dc] == 1:
                    visited[r + dr][c + dc] += 1
                # 빈 공간일 경우
                else:
                    if not visited[r + dr][c + dc]:
                        visited[r + dr][c + dc] = 1
                        q.append((r + dr, c + dc))

    return visited

answer = 0

while True:
    answer += 1

    air = []
    for r in range(1, N - 1):
        air.append((r, 0))
        air.append((r, M - 1))
    for c in range(1, M - 1):
        air.append((0, c))
        air.append((N - 1, c))

    # 1초마다 치즈가 녹는 시뮬레이션 (BFS) 수행
    visited = bfs(air)

    # for row in cheeze:
    #     print(row)
    # print()
    # for row in visited:
    #     print(row)
    # print()

    # 모든 치즈가 녹았는지 검사
    all_melted = True
    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 1:
                if visited[i][j] >= 2:
                    cheeze[i][j] = 0
                else:
                    all_melted = False

    if all_melted == True:
        break

print(answer)
