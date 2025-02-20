# 백준 1446번: 지름길

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

N, target = map(int, input().rstrip().split())
edges = []

vertices = set()
graph = defaultdict(dict)

for _ in range(N):
    start, end, cost = map(int, input().rstrip().split())

    if end > target: continue
    if end - start <= cost: continue
    vertices.add(start)
    vertices.add(end)
    edges.append((start, end, cost))

vertices.add(0)
vertices.add(target)
distances = {idx: int(1e9) for idx in vertices}
# print(distances)

for start in vertices:
    for end in vertices:
        if start < end:
            graph[start][end] = end - start

for start, end, cost in edges:
    graph[start][end] = min(graph[start][end], cost)

hq = [(0, 0)]

while hq:
    current_distance, current_vertex = heapq.heappop(hq)

    if distances[current_vertex] < current_distance: continue

    for next_vertex, next_distance in graph[current_vertex].items():
        distance = current_distance + next_distance
        if distance < distances[next_vertex]:
            distances[next_vertex] = distance
            heapq.heappush(hq, (distance, next_vertex))

print(distances[target])
