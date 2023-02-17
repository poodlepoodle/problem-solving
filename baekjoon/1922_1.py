import sys
import heapq

input = sys.stdin.readline

# 최대 10^3
N = int(input())

# 최대 10^5
M = int(input())

parents = [i for i in range(N + 1)]
edges = []

for _ in range(M):
    A, B, cost = map(int, input().rstrip().split())

    heapq.heappush(edges, (cost, A, B))

def find(x):
    X = x
    while parents[X] != X:
        X = parents[X]
    
    parents[x] = X
    return X

def union(A, B):
    parent_A = find(A)
    parent_B = find(B)

    if parent_A < parent_B:
        parents[parent_B] = parent_A
    else:
        parents[parent_A] = parent_B

mst = []

while edges:
    cost, A, B = heapq.heappop(edges)

    if find(A) != find(B):
        mst.append(cost)
        union(A, B)

    if len(mst) == N - 1:
        break

print(sum(mst))
