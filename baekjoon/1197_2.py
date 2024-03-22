# 백준 1197번: 최소 스패닝 트리 (2회차)

import heapq
import sys

input = sys.stdin.readline

# V <= 10^4, E <= 10^5
V, E = map(int, input().rstrip().split())

edges = []
for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    heapq.heappush(edges, (C, A, B))

parent = [idx for idx in range(V + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(A, B):
    find_A, find_B = find(A), find(B)

    if find_A != find_B:
        if find_A < find_B:
            parent[find_B] = find_A
        else:
            parent[find_A] = find_B

mst = []

while edges and len(mst) < V:
    C, A, B = heapq.heappop(edges)
    
    if find(A) != find(B):
        mst.append(C)
        union(A, B)

print(sum(mst))