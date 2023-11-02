# 백준 1922번: 네트워크 연결 (2회차)

import heapq
import sys

input = sys.stdin.readline

# N <= 10^3
N = int(input())

# M <= 10^5
M = int(input())

# 딱 봐도 최소 스패닝 트리 문제
edges = []

for _ in range(M):
    A, B, cost = map(int, input().rstrip().split())

    heapq.heappush(edges, (cost, A, B))

mst = []

# 아 생각해보니까 Kruskal은 유니온-파인드를 써야 한다...

parent = [i for i in range(N + 1)]

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(A, B):
    find_A, find_B = find(A), find(B)

    if find_A < find_B:
        parent[find_B] = find_A
    elif find_A > find_B:
        parent[find_A] = find_B

while len(mst) < N - 1:
    cost, A, B = heapq.heappop(edges)
    # print(cost, ':', A, B)

    if find(A) != find(B):
        union(A, B)
        mst.append(cost)

        # print(mst)

print(sum(mst))
