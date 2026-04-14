# 백준 1707번: 이분 그래프 (2회차)

import sys
sys.setrecursionlimit(2 * 10**4 + 1)
input = sys.stdin.readline

# K <= 5
K = int(input())

def is_bipartite_graph(N, edges):
    parents = [i for i in range(2 * N)]
    
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(a, b):
        A, B = find(a), find(b)

        if A == B: return
        elif A < B: parents[B] = A
        else: parents[A] = B
    
    for a, b in edges:
        a, b = a - 1, b - 1
        A, B = find(a), find(b)

        if A == B: return False

        union(A, B + N)
        union(B, A + N)

    return True

for _ in range(K):
    # V <= 2 * 10^4
    # E <= 2 * 10^5
    V, E = map(int, input().rstrip().split())

    edges = [list(map(int, input().rstrip().split())) for _ in range(E)]
    print('YES' if is_bipartite_graph(V, edges) else 'NO')
