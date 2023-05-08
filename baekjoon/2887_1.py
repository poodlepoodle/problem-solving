# 백준 2887번: 행성 터널

import sys
import heapq

input = sys.stdin.readline

# N <= 10^5
N = int(input())

planets = [[idx, *list(map(int, input().rstrip().split()))] for idx in range(N)]

# 모든 행성을 터널로 연결하는데 필요한 최소 비용 -> MST
# 정점의 개수 < 간선의 개수 -> 프림 알고리즘 써야겠다

nearest_x = sorted(planets, key=lambda x:x[1])
nearest_y = sorted(planets, key=lambda x:x[2])
nearest_z = sorted(planets, key=lambda x:x[3])

edges = []

for idx in range(N - 1):
    heapq.heappush(edges, (abs(nearest_x[idx][1] - nearest_x[idx + 1][1]), nearest_x[idx][0], nearest_x[idx + 1][0]))
    heapq.heappush(edges, (abs(nearest_y[idx][2] - nearest_y[idx + 1][2]), nearest_y[idx][0], nearest_y[idx + 1][0]))
    heapq.heappush(edges, (abs(nearest_z[idx][3] - nearest_z[idx + 1][3]), nearest_z[idx][0], nearest_z[idx + 1][0]))

# Union-Find 알고리즘
parent = [idx for idx in range(N)]

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a
    parent[b] = a

mst = []

while len(mst) < N - 1:
    cost, A, B = heapq.heappop(edges)

    if find(A) != find(B):
        mst.append(cost)
        union(A, B)

print(sum(mst))
