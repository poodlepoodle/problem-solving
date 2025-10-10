# 백준 1976번: 여행 가자

from collections import defaultdict
import sys

input = sys.stdin.readline

# N <= 2 * 10^2
N = int(input())
# M <= 10^3
M = int(input())

graph = defaultdict(list)
for i in range(N):
    row = list(map(int, input().rstrip().split()))
    for j in range(N):
        if row[j] == 1:
            graph[i + 1].append(j + 1)
            graph[j + 1].append(i + 1)
for key in graph.keys():
    graph[key] = list(set(graph[key]))

to_visit = list(map(int, input().rstrip().split()))

visited = [False for i in range(N + 1)]
def dfs(current): 
    # print('dfs()', current)
    visited[current] = True

    for nbh in graph[current]:
        if not visited[nbh]:
            dfs(nbh)

start = to_visit[0]
visited[start] = True
dfs(start)

answer = 'YES'
for city in to_visit[1:]:
    if not visited[city]:
        answer = 'NO'
        break
print(answer)
