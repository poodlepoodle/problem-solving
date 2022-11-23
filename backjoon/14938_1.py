import sys

def input(): return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())

items = list(map(int, input().split()))

distance = [[int(1e9) for _ in range(N)] for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    a, b = a - 1, b - 1

    distance[a][b] = l
    distance[b][a] = l

for k in range(N):
    distance[k][k] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

max_items = 0
for i in range(N):
    item = sum([items[j] for j in range(N) if distance[i][j] <= M])
    max_items = max(max_items, item)

print(max_items)
