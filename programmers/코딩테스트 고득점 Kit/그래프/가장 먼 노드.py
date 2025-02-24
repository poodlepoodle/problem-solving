# 프로그래머스 49189번: 가장 먼 노드

# 정점 갯수 = n <= 10^4
# 간선 갯수 <= 10^4

from collections import defaultdict
import heapq

def solution(n, edge):
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [int(1e9) for _ in range(n + 1)]
    edges = []
    heapq.heappush(edges, (0, 1))
    distances[1] = 0
    
    max_distance = -1
    while edges:
        current_distance, current_node = heapq.heappop(edges)
        
        if current_distance > distances[current_node]: continue
        
        for next_node in graph[current_node]:
            new_distance = current_distance + 1
            
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(edges, (new_distance, next_node))
                max_distance = max(max_distance, new_distance)
    
    return len([distance for distance in distances if distance == max_distance])
