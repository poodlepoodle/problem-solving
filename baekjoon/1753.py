# 백준 1753번: 최단경로

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
start = int(input())

graph = defaultdict(dict)
for _ in range(E):
    A, B, W = map(int, input().rstrip().split())

    if B not in graph[A]: graph[A][B] = W
    else: graph[A][B] = min(graph[A][B], W)

distances = [int(1e9) for _ in range(V + 1)]
hq = [(0, start)]
distances[start] = 0

while hq:
    current_distance, current_node = heapq.heappop(hq)

    if distances[current_node] < current_distance: continue

    for next_node, next_distance in graph[current_node].items():
        new_distance = current_distance + next_distance
        if new_distance < distances[next_node]:
            distances[next_node] = new_distance
            heapq.heappush(hq, (new_distance, next_node))

for distance in distances[1:]:
    print('INF' if distance >= int(1e9) else distance)
