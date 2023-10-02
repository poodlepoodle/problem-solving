# 백준 1277번: 발전소 설치

from collections import defaultdict
import heapq
import math
import sys

input = sys.stdin.readline

# N <= 10^3, W <= 10^4
N, W = map(int, input().rstrip().split())

M = float(input())

positions = [0]
for idx in range(1, N + 1):
    x, y = map(int, input().rstrip().split())
    positions.append((x, y))

graph = defaultdict(list)
for i in range(1, N + 1):
    xi, yi = positions[i]

    for j in range(1, N + 1):
        xj, yj = positions[j]

        cost = math.sqrt((xi - xj)**2 + (yi - yj)**2)
        if cost <= M:
            graph[i].append((j, cost))
            graph[j].append((i, cost))

for _ in range(W):
    A, B = map(int, input().rstrip().split())
    # A와 B는 가중치 0의 간선으로 추가

    graph[A].append((B, 0))
    graph[B].append((A, 0))
 
distance = [int(1e9) for _ in range(N + 1)]

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, current = heapq.heappop(q)

        if distance[current] < cost: continue
        distance[current] = cost

        for next, next_cost in graph[current]:
            if distance[next] > distance[current] + next_cost:
                distance[next] = distance[current] + next_cost
                heapq.heappush(q, (distance[current] + next_cost, next))

dijkstra(1)
print(int(distance[N] * 1000))
