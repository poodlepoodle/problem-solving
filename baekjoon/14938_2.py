import sys

input = sys.stdin.readline

# 지역의 개수 N, 예은이의 수색범위 M, 길의 개수 R
N, M, R = map(int, input().rstrip().split())

items = list(map(int, input().rstrip().split()))

# 정점 간의 최단거리 테이블
distance = [[int(1e9) for _ in range(N)] for _ in range(N)]

# 자기 자신으로 향하는 최단거리 -> 0
for k in range(N):
    distance[k][k] = 0

for _ in range(R):
    A, B, L = map(int, input().rstrip().split())
    distance[A - 1][B - 1] = L
    distance[B - 1][A - 1] = L

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

max_items = 0
for i in range(N):
    current_items = sum([items[j] for j in range(N) if distance[i][j] <= M])
    max_items = max(max_items, current_items)

print(max_items)
