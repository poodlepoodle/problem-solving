from collections import defaultdict
import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

V, E = map(int, input().split())

K = int(input())

graph = defaultdict(list)

for _ in range(E):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))

print(graph)

table = [int(1e9) for _ in range(V + 1)]

def dijkstra(start):
    heap = []

    global table
    table[start] = 0

    heapq.heappush(heap, (start, 0))

    while heap:
        A, A_cost = heapq.heappop(heap)

        if A_cost > table[A]: continue

        for B, B_cost in graph[A]:
            new_cost = A_cost + B_cost

            if new_cost < table[B]:
                table[B] = new_cost
                heapq.heappush(heap, (B, new_cost))

dijkstra(K)

for cost in table[1:]:
    print(cost if cost != int(1e9) else 'INF')
