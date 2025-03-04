# 백준 2098번: 외판원 순회

import sys

input = sys.stdin.readline

N = int(input()) # <= 16
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

def has_visited(visited, idx):
    return (visited & (1 << idx)) != 0

def visit(visited, idx):
    return visited | (1 << idx)

ALL_VISITED = (1 << N) - 1
INF = int(1e9)
# dp[current][visited]
# = visited 도시들을 방문한 상태에서 current 도시에 도달했을 때,
#   나머지 모든 정점을 거쳐서 출발 도시로 돌아가는 최소 비용
dp = [[None for _ in range(ALL_VISITED + 1)] for _ in range(N)]

def TSP(current, visited):
    # print(f'TSP({current}, {visited})')
    if visited == ALL_VISITED: return graph[current][0] or INF
    if dp[current][visited] != None: return dp[current][visited]

    min_distance = INF
    for next in range(N):
        if has_visited(visited, next) or (not graph[current][next]): continue
        next_visited = visit(visited, next)
        next_cost = graph[current][next] + TSP(next, next_visited)
        min_distance = min(min_distance, next_cost)

    dp[current][visited] = min_distance
    return min_distance

answer = TSP(0, 1 << 0)
print(answer)
