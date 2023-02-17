import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

q = deque()

# 최소 거리로 토마토를 전파시키면 10^3 * 10^3만큼만 계산하면 BFS로 문제 풀이 가능

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다
tomatoes = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((0, i, j))

total_days = 0

while q:
    day, i, j = q.popleft()

    if day > total_days:
        total_days = day

    if 0 <= i + 1 < N:
        if box[i + 1][j] == 0:
            q.append((day + 1, i + 1, j))
            box[i + 1][j] = 1
    if 0 <= i - 1 < N:
        if box[i - 1][j] == 0:
            q.append((day + 1, i - 1, j))
            box[i - 1][j] = 1
    if 0 <= j + 1 < M:
        if box[i][j + 1] == 0:
            q.append((day + 1, i, j + 1))
            box[i][j + 1] = 1
    if 0 <= j - 1 < M:
        if box[i][j - 1] == 0:
            q.append((day + 1, i, j - 1))
            box[i][j - 1] = 1

# 아직 익지 않은 토마토가 있는지 검사
finished = True
for row in box:
    if 0 in row:
        finished = False
print(total_days if finished else -1)
