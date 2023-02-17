import sys
import heapq
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

V, E = map(int, input().split())

# 시작점 K
K = int(input())

# 최단 거리 테이블 초기화
table = [INF] * (V + 1)

# 우선순위 큐 초기화
heap = []
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    # 최단 거리 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    table[start] = 0
    heapq.heappush(heap,(0, start))

    # 우선순위 큐가 비어있지 않을 동안 반복
    while heap:
        cost, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if table[now] < cost:
            continue

        for next_node, weight in graph[now]:
            # 현재 정점 까지의 가중치 cost + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치 (new_cost)
            new_cost = weight + cost
            # 다음 노드까지의 가중치 (new_cost)가 현재 기록된 값 보다 작으면 조건 성립
            if new_cost < table[next_node]:
                # 계산했던 new_cost를 가중치 테이블에 업데이트
                table[next_node] = new_cost
                # 다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입
                heapq.heappush(heap,(new_cost,next_node))

# 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    # (목적지 노드, 가중치) 형태로 저장
    graph[u].append((v, w))

dijkstra(K)
for i in range(1,V+1):
    print("INF" if table[i] == INF else table[i])
