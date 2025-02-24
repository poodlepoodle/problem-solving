# 프로그래머스 72413번: 합승 택시 요금

from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    # 정점 개수: n <= 10^2
    # 출발 정점: s
    # 두 사람의 도착 정점: a, b
    # 간선 개수 <= n^2 <= 10^4
    
    graph = {}
    distances = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

    for c, d, cost in fares:
        if c not in graph: graph[c] = {}
        if d not in graph[c]: graph[c][d] = cost
        else: graph[c][d] = min(graph[c][d], cost)
        
        if d not in graph: graph[d] = {}
        if c not in graph[d]: graph[d][c] = cost
        else: graph[d][c] = min(graph[d][c], cost)

    def dijkstra(start):
        edges = []    
        distances[start][start] = 0
        heapq.heappush(edges, (0, start))
    
        while edges:
            current_distance, current_node = heapq.heappop(edges)
            
            if distances[start][current_node] < current_distance: continue
            
            for next_node, next_distance in graph[current_node].items():
                new_distance = current_distance + next_distance
                
                if new_distance < distances[start][next_node]:
                    distances[start][next_node] = new_distance
                    heapq.heappush(edges, (new_distance, next_node))
                    
    dijkstra(s)
    dijkstra(a)
    dijkstra(b)

    answer = int(1e9)
    for i in range(1, n + 1):
        answer = min(answer, distances[s][i] + distances[a][i] + distances[b][i])
        
    return answer
