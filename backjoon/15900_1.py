from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 트리의 정점 개수 N은 최대 5 * 10^5
N = int(input())

# 간선 정보 그래프
graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
answer = 0

def dfs(current, level):
    cnt = 0

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            cnt += 1
            dfs(neighbor, level + 1)

    if not cnt:
        global answer
        answer += level
    
visited[1] = True
dfs(1, 0)

print('Yes' if answer % 2 else 'No')
